import os
import asyncio
import shelve
import time
import itertools
import hashlib
from contextlib import contextmanager
import threading
import collections

import ewsgi
import edb
from constants import *
from scripts.segments import Segment
import midas_conn

import filelock
import csv
import re
import json
import pickle
import datetime

cell_storage_loc = '/data3/bpm/publish/cells/'
group_csv_storage_loc = '/data3/bpm/publish/groups_data/'
group_storage_loc = '/data3/bpm/publish/groups/'


class Pid2IdIsNullException(Exception):
    pass


class MidasCanceledException(Exception):
    pass


if not os.path.exists(cell_storage_loc):
    raise NotADirectoryError(cell_storage_loc)

if not os.path.exists(group_csv_storage_loc):
    raise NotADirectoryError(group_csv_storage_loc)

if not os.path.exists(group_storage_loc):
    raise NotADirectoryError(group_storage_loc)

if not os.access(cell_storage_loc, os.W_OK):
    raise PermissionError('cannot write in "%s"' % cell_storage_loc)

if not os.access(group_storage_loc, os.W_OK):
    raise PermissionError('cannot write in "%s"' % group_storage_loc)

if not os.access(group_csv_storage_loc, os.W_OK):
    raise PermissionError('cannot write in "%s"' % group_csv_storage_loc)


def get_source(book):
    source_chn = [BOOK_STT_DAILY, BOOK_STT_MONTH, BOOK_STT_PULLED]
    source_zy = [BOOK_STT_DAILY_ZY, BOOK_STT_MONTH_ZY, BOOK_STT_PULLED_ZY]

    if book in source_chn:
        return 'chain'
    if book in source_zy:
        return 'zy'
    if book is BOOK_STT_PULLED_MERGE:
        return 'archive'

    return None


def get_slot_key_dir(slot_task_key, chain):
    max_t = max(map(int, re.findall(r'=(\d*)', slot_task_key, )))
    cell_dir = os.path.join(cell_storage_loc, str(chain), str(max_t % 1000))
    try:
        os.mkdir(cell_dir)
    finally:
        return cell_dir


def get_moviecode_in_cell_name(cell_name):
    return cell_name.split('_')[4]


def row_get_showyear(date_string):
    return date_string[:4]


def row_get_showseason(date_string):
    r = int(date_string[4:6]) / 3
    if r > 3:
        return int('%s4' % date_string[:4])
    elif r > 2:
        return int('%s3' % date_string[:4])
    elif r > 1:
        return int('%s2' % date_string[:4])
    else:
        return int('%s1' % date_string[:4])


def row_get_imax(moviecode_string):
    if moviecode_string[4] in ('3', '4', 'n', 'o', 'x', 'y'):
        return 1
    return 0


def cell_row_cast(row):
    """
    账本  票房日期  票房月  排次号       影院编码  院线    省份      设备 场  人  收     影厅数  排次号ID
    1,   20161102,201611,051301092016,22110201,223456,220000000,1,   1, 12, 36000, 1,     20948
    :param row:
    :return:
    """
    row = row.split(',')
    if len(row) != 14:
        raise ValueError('cell 原始数据错误', row)

    cast_row = []
    for i, e in enumerate(row):
        # 除去第四列影片排次号需要作为字符串导入，其余列都是整型数
        if i != 3:
            cast_row.append(int(e))
        else:
            cast_row.append(e)
    return cast_row


class MoviecodeError(Exception):
    pass


class PidError(Exception):
    pass


class CinemaError(Exception):
    pass


class GroupLoadFile(object):
    def __init__(self, label_identify):
        self.rotate_count = 0
        self.identify = label_identify
        self.fh, self.cfh = None, None
        self.label = 'bpm_interior_publish_%s' % label_identify

    @contextmanager
    def open(self):
        self.fh = open(self.filename, 'w')
        self.cfh = csv.writer(self.fh)
        yield
        self.close()

    def write(self, rows):
        self.cfh.writerows(rows)

    def close(self):
        self.fh.close()

    @property
    def filename(self):
        file_path = os.path.join(group_csv_storage_loc, '%s.csv' % self.label)

        return file_path


class Monitor(object):
    touch_lock = threading.Lock()

    def __init__(self, name, interval=None):

        self.name = name

        self.init_flag = False
        self.init_event = asyncio.Event()
        self.update_event = asyncio.Event()
        self.update_interval = interval
        self.last_update_time = None
        self.last_used_time = None
        self.max_used_time = 0

        return

    @asyncio.coroutine
    def wait(self):

        if self.update_interval == None:

            yield from self.update_event.wait()

        else:

            try:
                yield from asyncio.wait_for(self.update_event.wait(), self.update_interval)
            except asyncio.TimeoutError:
                pass

        return

    @contextmanager
    def init(self):

        print(self.name, 'FIRST START')
        st = time.time()
        yield
        ed = time.time()
        print(self.name, 'END')

        self.last_used_time = ed - st
        self.last_update_time = ed

        self.init_flag = True
        self.init_event.set()

        return

    @contextmanager
    def _update(self):

        print(self.name, 'START')
        st = time.time()
        yield
        ed = time.time()
        print(self.name, 'END')

        self.last_used_time = ed - st
        self.max_used_time = max(self.max_used_time, self.last_used_time)
        self.last_update_time = ed

        return

    def update(self):

        if self.init_flag:
            return self._update()

        return self.init()

    def touch(self):

        with self.touch_lock:
            self.update_event.set()
            self.update_event.clear()

        return


class App(ewsgi.WsgiServer):
    def __init__(self):

        super().__init__()
        self.bpm_conn = edb.Database('bpm')
        self.pub_conn = edb.Database('pub')
        self.bpm_movie_conn = edb.Database('bpm_movie')

        self.fdm_conn = edb.Database('fdm')
        # self.etl_conn = dbconn.Database('etl')
        self.mds_conn = None

        # self.db = Database()
        self.cells_base_file = "cells_pub_std"

        self.cells = {}
        self.group = None

        self.slot_count = 0

        self.pid2moviecode = {}
        self.moviecode2mix_mode = {}
        self.moviecodeMonth2pid = {}
        # {'GF0010202':{'0123467a2018':set([('中数','租赁'),('院线','自购')])}

        self.day_monitor_task_types = [TASK_DAILY_LEASE_VS_LEASE]
        self.day_slots = collections.defaultdict(lambda: dict.fromkeys(self.day_monitor_task_types))
        # {(date, chain): {TaskType:TaskID, ...}}
        self.day_monitor = Monitor('DAY', 30)

        self.month_monitor_task_types = [TASK_MONTH_LEASE_VS_LEASE, TASK_MONTH_MON_VS_DAY]
        self.month_slots = collections.defaultdict(lambda: dict.fromkeys(self.month_monitor_task_types))
        # {(month, chain): {TaskType:TaskID, ...}}
        self.month_monitor = Monitor('MTH', 40)

        self.stopscreen_monitor_task_types = [CHAIN_RELEASE_COMPARE_CHAIN_MONTH, CHAIN_RELEASE_COMPARE_ZY_RELEASE]
        self.stopscreen_slots = collections.defaultdict(lambda: dict.fromkeys(self.stopscreen_monitor_task_types))
        # {(project, chain): {TaskType:TaskID, ...}}
        self.stopscreen_monitor = Monitor('STP', 100)

        self.slot_dir = {}

        self.project_mix_mode = {}
        # {(moviecode, chain): {TaskType:TaskID, ...}}
        self.project_monitor = Monitor('PRJ', 2 * 60)

        self.pid_id_map = {}

        # self.update_event = asyncio.Event()
        self.cell_monitor = Monitor('CLL')

        self.group_monitor = Monitor('GRP')
        self.load_group_monitor = Monitor('LGP')

        self.clean_group_monitor = Monitor('CGP', 60)

        return

    def init_async_work(self):

        asyncio.Task(self.monitor_project_info())
        asyncio.Task(self.monitor_day_task())
        asyncio.Task(self.monitor_month_task())
        asyncio.Task(self.monitor_stopscreen_task())
        asyncio.Task(self.generate_cells())
        asyncio.Task(self.generate_groups())
        asyncio.Task(self.load_groups())
        asyncio.Task(self.clean_groups())

        return

    def get_latest_task(self, monitor_task_types, not_scanned=False):
        if not_scanned:
            tasks = self.bpm_conn(
                f'''select `target`, `unit`, `period`,  `type`, max(`id`) as `tid` from `bpm_statistics_tasks` 
                    where `type` in ({','.join(map(str, monitor_task_types))}) and `status` = %s and `state` = %s
                    and `scan` = %s
                    group by `target`, `unit`, `period`, `type` ''',
                (STATUS_NORMAL, STATE_STABLED, NOT_SCANNED)
            )

        else:
            tasks = self.bpm_conn(
                f'''select `target`, `unit`, `period`,  `type`, max(`id`) as `tid` from `bpm_statistics_tasks` 
                    where `type` in ({','.join(map(str, monitor_task_types))}) and `status` = %s and `state` = %s
                    group by `target`, `unit`, `period`, `type` ''',
                (STATUS_NORMAL, STATE_STABLED)
            )
        return tasks

    # 补充排次号数据组合缺失模式的两种情况，1，排次号错误，添加默认模式 2，复映排次号缺失月份对应模式，添加默认模式
    def repair_moviecode_mode(self, cell):
        # 1，排次号错误，添加默认模式
        if cell['moviecode'] not in self.moviecode2mix_mode:  # 未知影片赋予默认值
            self.moviecode2mix_mode.setdefault(cell['moviecode'], Segment())
            self.moviecode2mix_mode[cell['moviecode']][:] = set([('zy', DEVICE_LEASED), ('chain', DEVICE_OWNED)])

        # 2，复映排次号缺失月份对应模式，添加默认模式
        if not self.moviecode2mix_mode[cell['moviecode']][cell['showmonth']]:
            self.moviecode2mix_mode[cell['moviecode']][cell['showmonth']:] = set(
                [('zy', DEVICE_LEASED), ('chain', DEVICE_OWNED)])

    def get_cell_pinfo(self, moviecode, showmonth):
        if moviecode not in self.moviecodeMonth2pid:
            return {'pid': 0, 'id': 0, 'ptype': 0, 'pclass': 0, 'pfamily': 0}
        if not self.moviecodeMonth2pid[moviecode][showmonth]:
            return {'pid': 0, 'id': 0, 'ptype': 0, 'pclass': 0, 'pfamily': 0}

        back_dict = self.moviecodeMonth2pid[moviecode][showmonth]
        if not self.pid_id_map.get(back_dict['pid']):
            res = self.fdm_conn('select pid_id, id from fdm_project_id where pid_id=%s', back_dict['pid'])
            if res:
                pid2id = res[0]['id']
            else:
                raise Pid2IdIsNullException
        else:
            pid2id = self.pid_id_map.get(back_dict['pid'])

        back_dict['id'] = pid2id
        return back_dict

    @asyncio.coroutine
    def monitor_project_info(self):

        while (True):
            with self.project_monitor.update():
                imax_way = {
                    IMAX_CHAIN: {('chain', DEVICE_LEASED), ('chain', DEVICE_OWNED)},
                    IMAX_ZHONGYING: {('zy', DEVICE_LEASED), ('zy', DEVICE_OWNED)},
                    IMAX_DEFAULT: {('zy', DEVICE_LEASED), ('chain', DEVICE_OWNED)}
                }
                pid_moivecode = self.fdm_conn('''
                                select tm.pid as pid, lower(tm.code) as moviecode, tm.edition as edition,
                                 tm.zone as zone,tp.ptype as ptype, tp.pclass as pclass, tp.pfamily as pfamily  
                                from fdm_moviecode tm left join fdm_project tp 
                                on tm.pid = tp.pid where tp.ptype != 99
                                ''')

                imax_option = dict(self.bpm_movie_conn.tuple(
                    '''select t1.pid as pid, t1.settlement_way_imax as imax_way from 
                        bpm_options t1 left join (select pid, max(id) as id from bpm_options GROUP by pid) t2
                        on t1.id=t2.id where  t1.settlement_way_imax in (%s,%s)''', (IMAX_CHAIN, IMAX_ZHONGYING)))

                returned_project = self.bpm_movie_conn(
                    '''select pid, start_month, end_month from bpm_project_returned''')

                returned_project_dict = {r['pid']: (r['start_month'], r['end_month']) for r in returned_project}

                pid2moviecode = {}
                moviecode2mix_mode = {}
                moviecodeMonth2pid = {}
                for pc in pid_moivecode:
                    month_tuple = returned_project_dict.get(pc['pid'], (None, None))
                    if pc['edition'] in (IMAXJP, IMAX2D, IMAX3D):  # 如果排次号的版本为imax,查找指定的组合方法，为指定选择默认
                        im_v = imax_option.get(pc['pid'], IMAX_DEFAULT)
                    else:
                        im_v = IMAX_DEFAULT

                    pid2moviecode.setdefault(pc['pid'], {})

                    pid2moviecode[pc['pid']][pc['moviecode']] = (month_tuple, imax_way.get(im_v))
                    # back_project_info.append((month_tuple[0], month_tuple[1],pc['moviecode'],pc['pid'],pc['zone']))

                    moviecode2mix_mode.setdefault(pc['moviecode'], Segment())
                    moviecode2mix_mode[pc['moviecode']][month_tuple[0]:month_tuple[1]] = imax_way.get(im_v)

                    moviecodeMonth2pid.setdefault(pc['moviecode'], Segment())
                    # 复映的pid, 缺少排次号，但是该排次号在复映期间有票房
                    moviecodeMonth2pid[pc['moviecode']][month_tuple[0]:month_tuple[1]] = {
                        'pid': pc['pid'],
                        'ptype': pc['ptype'],
                        'pclass': pc['pclass'],
                        'pfamily': pc['pfamily']
                    }

                changed = bool(self.pid2moviecode != pid2moviecode)

                changed_pid = bool(self.moviecodeMonth2pid != moviecodeMonth2pid)
                self.moviecode2mix_mode = moviecode2mix_mode

                self.pid_id_map = dict(self.fdm_conn.tuple('select pid, id from fdm_project_id'))

                if changed:
                    self.pid2moviecode = pid2moviecode
                    if self.project_monitor.init_flag == False:
                        self.cell_monitor.touch()

                if changed_pid:
                    self.moviecodeMonth2pid = moviecodeMonth2pid
                    if self.group_monitor.init_flag == False:
                        self.group_monitor.touch()

            yield from self.project_monitor.wait()

    @asyncio.coroutine
    def monitor_day_task(self):

        with self.day_monitor.init():
            tasks = self.get_latest_task(self.day_monitor_task_types)

            for _ in tasks:
                _['period'] = _['period'].strftime('%Y%m%d')
                if _['period'] < '20171201':
                    continue
                self.day_slots[(int(_['unit']), int(_['period']))][_['type']] = _['tid']

        while (True):

            yield from self.day_monitor.wait()
            changed = False

            with self.day_monitor.update():
                tasks = self.get_latest_task(self.day_monitor_task_types, True)
                for _ in tasks:
                    _['period'] = _['period'].strftime('%Y%m%d')
                    if self.day_slots[(int(_['unit']), int(_['period']))][_['type']] != _['tid']:
                        changed = True
                        self.day_slots[(int(_['unit']), int(_['period']))][_['type']] = _['tid']

            if changed:
                self.cell_monitor.touch()

    @asyncio.coroutine
    def monitor_month_task(self):

        with self.month_monitor.init():
            tasks = self.get_latest_task(self.month_monitor_task_types)

            for _ in tasks:
                _['period'] = _['period'].strftime('%Y%m%d')
                self.month_slots[(int(_['unit']), int(_['period'][:6]))][_['type']] = _['tid']

        while (True):

            yield from self.month_monitor.wait()
            changed = False

            with self.month_monitor.update():
                tasks = self.get_latest_task(self.month_monitor_task_types, True)
                for _ in tasks:
                    _['period'] = _['period'].strftime('%Y%m%d')
                    if self.month_slots[(int(_['unit']), int(_['period'][:6]))][_['type']] != _['tid']:
                        changed = True
                        self.month_slots[(int(_['unit']), int(_['period'][:6]))][_['type']] = _['tid']

            if changed:
                self.cell_monitor.touch()

    @asyncio.coroutine
    def monitor_stopscreen_task(self):

        with self.stopscreen_monitor.init():
            tasks = self.get_latest_task(self.stopscreen_monitor_task_types)
            wanpian_pids = self.bpm_movie_conn('''select pid from bpm_wanpian_project''')
            wanpian_pids_sets = set([p['pid'] for p in wanpian_pids])

            for _ in tasks:
                if _['target'] in wanpian_pids_sets:  # 过滤完片归档的项目
                    continue
                self.stopscreen_slots[(int(_['unit']), _['target'])][_['type']] = _['tid']

        while (True):
            yield from self.stopscreen_monitor.wait()
            changed = False
            with self.stopscreen_monitor.update():
                tasks = self.get_latest_task(self.stopscreen_monitor_task_types, True)
                wanpian_pids = self.bpm_movie_conn('''select pid from bpm_wanpian_project''')
                wanpian_pids_sets = set([p['pid'] for p in wanpian_pids])
                for _ in tasks:
                    if _['target'] in wanpian_pids_sets:  # 过滤完片归档的项目
                        continue
                    if self.stopscreen_slots[(int(_['unit']), _['target'])][_['type']] != _['tid']:
                        changed = True
                        self.stopscreen_slots[(int(_['unit']), _['target'])][_['type']] = _['tid']
            if changed:
                self.cell_monitor.touch()

    def get_moviecode_id(self, moviecode):
        """
        :param mc_in_cell: set
        :return:
        """
        r = self.bpm_conn('select `id`, `code` from `uni_moviecodes` where `code` = %s', moviecode)
        if r:
            return r[0]['id']
        else:
            conn = edb.Database('w1_etl')
            try:
                moviecode_id = conn('select `id`, `code` from `obj_moviecodes` where `code` = %s', moviecode)

                if moviecode_id:
                    return moviecode_id[0]['id']
                else:
                    return conn('insert into `obj_moviecodes` (`id`, `code`) value (null, %s)', moviecode)

            except Exception as e:
                print(str(e))
            finally:
                conn.tvar.conn.close()

        raise MoviecodeError

    def construct_cell_base(self, slots):
        all_cm_city = dict(self.bpm_conn.tuple('select `code`, `city` from `uni_cinemas`'))
        self.mds_conn = midas_conn.Midas('bestine')
        with shelve.open(self.cells_base_file) as cells_base:

            slot_current = 0
            for slot, tasks, slot_task_key in slots:
                slot_current += 1
                print('slots progress: %s / %s' % (slot_current, self.slot_count))
                slot_dir = get_slot_key_dir(slot_task_key, slot[0])
                self.slot_dir[slot_task_key] = slot_dir

                slot_task_key_dir = os.path.join(slot_dir, slot_task_key)
                query_slice = {
                    'dim_cell_row': ' `book`, `showdate`, `showmonth`, `moviecode`, `cinema`, `chain`, `province`, `device`, sum(`shows`), sum(`audience`), sum(`revenue`), count(distinct(`hall`)) as hall_cnt ',
                    'group_cell_row': ' `book`, `showdate`, `showmonth`, `moviecode`, `cinema`, `chain`, `province`, `device` ',

                    'day': {
                        'dim': ' `showdate`, `showmonth`, `moviecode`, `chain`, `book`, `device` ',
                        'dim_cond': '`chain` = %s and `showdate` = %s and `book` in (1, 3)' % slot,
                        'row_cond': ' `moviecode` = %s and `showdate` = %s and `showmonth` = %s and `chain` = %s and `book` = %s and `device` = %s '
                    },
                    'mon': {
                        'dim': ' `showmonth`, `moviecode`, `chain`, `book`, `device`',
                        'dim_cond': '`chain` = %s and `showmonth` = %s and `book` in (2, 6)' % slot,
                        'row_cond': ' `moviecode` = %s and `chain` = %s and `showmonth` =%s and `book` = %s and `device` = %s '
                    },
                    'scn': {
                        'dim': ' `showmonth`, `moviecode`, `chain`, `book`, `device` ',
                        'dim_cond': f'''`chain` = {slot[0]} and `moviecode` in ('{ "','".join(self.pid2moviecode[slot[1]].keys()) if isinstance(slot[1], str) else ''}') and `book` in (4, 7, 8 )''',
                        'row_cond': ' `moviecode` = %s and `chain` = %s and `showmonth` =%s and `book` = %s and `device` = %s '
                    }
                }

                if slot_task_key not in cells_base:
                    if not os.path.exists(slot_task_key_dir):
                        os.makedirs(slot_task_key_dir)

                    with filelock.FileLock(os.path.join(slot_dir, '%s.lock' % slot_task_key)):

                        try:
                            with open(os.path.join(slot_task_key_dir, "cell.info")) as ifp:
                                cells_info = json.load(ifp)
                        except FileNotFoundError:
                            cells_info = []

                            data_lv = slot_task_key[:3]
                            task_dimension = self.mds_conn(
                                f'''select {query_slice[data_lv]['dim']}
                                  from `stt_boxoffice` 
                                  where {query_slice[data_lv]['dim_cond']} 
                                  group by {query_slice[data_lv]['dim']}
                                  '''
                            )

                            cell_current, cell_all = 0, len(task_dimension)
                            for dim in task_dimension:
                                cell_current += 1
                                print('slots progress: %s / %s, cells progress: %s / %s' % (
                                slot_current, self.slot_count, cell_current, cell_all))
                                book_source = get_source(dim['book'])
                                if book_source is None:
                                    continue

                                # cell_name 的组成与 dim 是一致的，可以认为根据 cell_name 即可重新获取到 cell
                                if data_lv == 'day':
                                    args = (
                                        dim['moviecode'], dim['showdate'], dim['showmonth'], dim['chain'], dim['book'],
                                        dim['device']
                                    )
                                    cell_name = f"{book_source}_{dim['book']}_{dim['showdate']}_{dim['chain']}_{dim['moviecode']}_{dim['device']}"
                                else:
                                    args = (
                                        dim['moviecode'], dim['chain'], dim['showmonth'], dim['book'], dim['device']
                                    )
                                    cell_name = f"{book_source}_{dim['book']}_{dim['showmonth']}_{dim['chain']}_{dim['moviecode']}_{dim['device']}"

                                cell_info = {
                                    'cell_name': cell_name,
                                    'slot_key': slot_task_key,
                                    'slot_dir': slot_task_key_dir.replace(cell_storage_loc, ''),
                                    'book': dim['book'], 'source': book_source, 'data_level': data_lv,
                                    'showmonth': dim['showmonth'],
                                    'chain': dim['chain'], 'moviecode': dim['moviecode'], 'device': dim['device'],
                                }

                                cell_csv_pth = os.path.join(slot_task_key_dir, cell_name + '.csv')
                                cell_rows = self.mds_conn(
                                    f'''select {query_slice['dim_cell_row']}
                                    from stt_boxoffice
                                    where {query_slice[data_lv]['row_cond']}
                                    group by {query_slice['group_cell_row']}
                                    ''', args
                                )

                                showdates = set()
                                cinemas = set()
                                chains = set()
                                shengs = set()
                                cnt = 0

                                moviecode_id = self.get_moviecode_id(cell_rows[0]['moviecode'])

                                with open(cell_csv_pth, 'w') as cell_fp:
                                    csv_writer = csv.writer(cell_fp)
                                    result = []
                                    for r in cell_rows:
                                        showdates.add(int(r['showdate']))
                                        cinemas.add(int(r['cinema']))
                                        chains.add(int(r['chain']))
                                        shengs.add(int(r['province']))
                                        cnt += 1
                                        r['moviecode_id'] = moviecode_id
                                        try:
                                            r['city'] = int(all_cm_city[r['cinema']])
                                        except:
                                            r['city'] = 0
                                        result.append(tuple(r.values()))

                                    csv_writer.writerows(result)

                                cinemas = sorted(list(cinemas))
                                firstdate = min(showdates)
                                lastdate = max(showdates)
                                showdates = sorted(list(showdates))
                                shengs = sorted(list(shengs))
                                ex_info = {
                                    'firstdate': firstdate,
                                    'lastdate': lastdate,
                                    'showdates': showdates,
                                    'cinemas': cinemas,
                                    'shengs': shengs,
                                    'rows': cnt,
                                }
                                cell_info.update(ex_info)
                                with open(os.path.join(slot_task_key_dir, '%s.info' % cell_name), 'wb') as fp:
                                    pickle.dump(cell_info, fp)

                                cell_info.pop('showdates')
                                cell_info.pop('cinemas')
                                cell_info.pop('shengs')

                                cells_info.append(cell_info)

                            with open(os.path.join(slot_task_key_dir, "cell.info"), 'w') as ifp:
                                json.dump(cells_info, ifp)

                        cells_base[slot_task_key] = cells_info

    @asyncio.coroutine
    def generate_cells(self):

        yield from self.project_monitor.init_event.wait()
        yield from self.day_monitor.init_event.wait()
        yield from self.month_monitor.init_event.wait()
        yield from self.stopscreen_monitor.init_event.wait()

        while (True):
            try:
                with self.cell_monitor.update():
                    self.slot_count = 0
                    day_slots = list(self.parse_slots(self.day_slots, 'day'))
                    month_slots = list(self.parse_slots(self.month_slots, 'mon'))
                    stopscreen_slots = list(self.parse_slots(self.stopscreen_slots, 'scn'))

                    # create new cell
                    self.construct_cell_base(itertools.chain(day_slots, month_slots, stopscreen_slots))

                    # generate
                    stopscreens = {}
                    for (chain, pid), tasks, slot_task_key in stopscreen_slots:
                        for moviecode, ((st, ed), mix_mode) in self.pid2moviecode[pid].items():
                            stopscreens.setdefault((moviecode, int(chain)), Segment())
                            stopscreens[(moviecode, int(chain))][st:ed] = True

                    monthreported = [(month, chain) for (chain, month), tasks, slot_task_key in month_slots]
                    monthreported = set(monthreported)

                    with shelve.open(self.cells_base_file) as cells_base:
                        cells = []
                        for slot, tasks, slot_task_key in itertools.chain(day_slots, month_slots, stopscreen_slots):
                            for cell in cells_base[slot_task_key]:

                                # DAY MONTH STOPSCREEN
                                #  y
                                #  y   y
                                #  y   y     y

                                # 补齐缺失moviecode组合模式为默认组合
                                self.repair_moviecode_mode(cell)

                                if cell['data_level'] == 'day' and (cell['showmonth'], cell['chain']) in monthreported:
                                    continue

                                if cell['data_level'] != 'scn':
                                    mc_segment = stopscreens.get((cell['moviecode'], cell['chain']), Segment())
                                    if mc_segment[cell['showmonth']]:
                                        continue

                                if (cell['source'], cell['device']) not in self.moviecode2mix_mode[cell['moviecode']][
                                    cell['showmonth']]:
                                    continue

                                cells.append(cell)
                        self.cells = cells
                    self.group_monitor.touch()
                yield from self.cell_monitor.wait()

            except MoviecodeError:
                yield from asyncio.sleep(300)
            except CinemaError:
                yield from asyncio.sleep(300)

    def parse_slots(self, slot, data_level):
        for k, v in slot.items():

            if None in list(v.values()):
                continue

            slot_task_key = '&'.join(['%s=%s' % (k, v) for k, v in sorted(v.items())])
            self.slot_count += 1
            yield k, v, '%s@%s' % (data_level, slot_task_key)

        return ''

    @asyncio.coroutine
    def generate_groups(self):
        while (True):
            with self.group_monitor.update():
                cells_info = self.cells_info_scan()
                self.group = self.construct_groups(cells_info)
                self.load_group_monitor.touch()

            yield from self.group_monitor.wait()

    def cells_info_scan(self):
        cells_info = []

        for cell in self.cells:
            with filelock.FileLock(os.path.join(self.slot_dir[cell['slot_key']], '%s.lock' % cell['slot_key'])):
                cell_info_path = os.path.join(cell_storage_loc, cell['slot_dir'], '%s.info' % cell['cell_name'])

                with open(cell_info_path, 'rb') as cfp:
                    cell_info = pickle.load(cfp)
                    cells_info.append(cell_info)

        return cells_info

    @staticmethod
    def load_group_from_json(md5):
        with open(os.path.join(group_storage_loc, md5 + '.json')) as gfp:
            raw_g = json.load(gfp)

        g = set()
        for cell in raw_g:
            converted_c = (cell[0],
                           cell[1],
                           # json 解析出来的结构是 list，这里需要做一次转换，变成 tuple
                           tuple(tuple(e) for e in cell[2]),
                           tuple(tuple(e) for e in cell[3]))
            g.add(converted_c)

        return g

    def construct_groups(self, cells_info):
        """
        :param cells_info:
        [
            {
                <cell_info>,
            },
        ]
        :return:
        [
            (slot_key, cell_name, ((str<pinfo_property>, int<pinfo_value>), ...), ((int<cinema_code>, int<city_code>), ...))
        ]
        """
        group = set()

        for cell_info in cells_info:
            pinfo = tuple(
                sorted(
                    [(prop, val) for prop, val in
                     self.get_cell_pinfo(cell_info['moviecode'], cell_info['showmonth']).items()]
                )
            )

            group.add((
                cell_info['slot_key'],
                cell_info['cell_name'],
                (
                    ('path', os.path.join(cell_storage_loc, cell_info['slot_dir'], '%s.csv' % cell_info['cell_name'])),
                    ('book', cell_info['book'],),
                    ('source', cell_info['source'],),
                    ('data_level', cell_info['data_level'],),
                    ('firstdate', cell_info['firstdate'],),
                    ('showmonth', cell_info['showmonth'],),
                    ('chain', cell_info['chain'],),
                    ('moviecode', cell_info['moviecode'],),
                    ('device', cell_info['device'],)
                ),
                pinfo
            ))

        return group

    def diff_group(self, g_base, g_dest):
        if g_base == g_dest:
            return {}

        diff_in_base = g_base - g_dest
        diff_in_now = g_dest - g_base
        going_groups = collections.defaultdict(lambda: {'to_add': set(), 'to_del': set()})

        for c in g_base:
            if c in diff_in_base:
                going_groups[get_moviecode_in_cell_name(c[1])]['to_del'].add(c)
        for c in g_dest:
            if c in diff_in_now:
                going_groups[get_moviecode_in_cell_name(c[1])]['to_add'].add(c)

        return going_groups

    @asyncio.coroutine
    def load_groups(self):
        """
            (
            slot_key, cell_name,
            (str<cell_property>, auto<cell_value>),
            ((str<pinfo_property>, int<pinfo_value>), ...),
            ((int<cinema_code>, int<city_code>), ...)
            )
        :return:
        """
        while True:
            with self.load_group_monitor.update():
                # 如果最近的一次 groups 导入状态为 invalid 状态，说明 midas 出现过未知错误
                latest_group = self.pub_conn('select * from publish_groups order by id desc limit 1')[0]
                if latest_group['status'] != STATUS_INVALID:
                    self.do_load(latest_group['groups'])
            yield from self.load_group_monitor.wait()

    def do_load(self, g_base_md5):
        self.mds_conn = midas_conn.Midas('bestine')
        g_base = self.load_group_from_json(g_base_md5)

        going_groups = self.diff_group(g_base, self.group)

        if going_groups:
            going_groups_succ, going_groups_fail, going_groups_all = 0, 0, len(going_groups)
            for mc, cells in going_groups.items():

                g_dest = tuple(g_base | cells['to_add'] - cells['to_del'])
                g_dest_md5 = hashlib.md5(json.dumps(g_dest).encode()).hexdigest()
                g_id = self.pub_conn('insert ignore into publish_groups value (null, %s, %s, %s)',
                                     (g_dest_md5, STATUS_INVALID, datetime.datetime.now()))

                with open(os.path.join(group_storage_loc, g_dest_md5 + '.json'), 'w') as gfp:
                    json.dump(g_dest, gfp)

                g_load = GroupLoadFile(g_id)

                self.group_data_combination(cells['to_add'], cells['to_del'], g_load)

                try:
                    self.mds_conn.upload_csv('bpm_interior_publish_boxoffice', g_load.label, g_load.filename)
                    while True:
                        ups = self.mds_conn.get_upload_status(g_load.label)
                        if not ups:
                            time.sleep(1)

                        if ups['State'] == 'FINISHED':
                            going_groups_succ += 1
                            g_base = set(g_dest)
                            self.pub_conn('update publish_groups set status = %s where id = %s',
                                          (STATUS_VALID, g_load.identify))
                            print('[进度]  成功:%d/失败:%d/总数:%d' % (going_groups_succ, going_groups_fail, going_groups_all))
                            break

                        if ups['State'] == 'CANCELLED':
                            going_groups_fail += 1
                            g_base = set(g_dest)
                            self.pub_conn('update publish_groups set status = %s where id = %s',
                                          (STATUS_UPLOAD_FAILED, g_load.identify))
                            print('[进度]  成功:%d/失败:%d/总数:%d' % (going_groups_succ, going_groups_fail, going_groups_all))
                            break

                        time.sleep(0.5)
                except Exception as err:
                    print(err)
                    raise

    def group_data_combination(self, add_list, delete_list, g_load):
        """
        0)账本  1)票房日期 2)票房月 3)排次号      4)影院编码 5)院线  6)省     7)设备 8)场  9)人  10)收  11)影厅数  12)排次号ID  13) 城市
        1,      20161102, 201611, 051301092016,22110201, 223456,220000000,1,     1,   12,   36000, 1,         20948        110000000
        :param add_list:
        :param delete_list:
        :return:
        """

        enum_box = {
            'data_lv': {
                'day': 1, 'mon': 2, 'scn': 3
            },
            'source': {
                'chain': 1, 'zy': 2, 'archive': 3
            }
        }
        with g_load.open():

            for cell in add_list:
                cinfo = dict(cell[2])
                pinfo = dict(cell[3])

                result = []
                with open(cinfo['path']) as cell_data:
                    for rw in cell_data:  # 拼接需要的数据
                        rw = cell_row_cast(rw)
                        # 旧数据中存在不合法的影院编码
                        if rw[4] > 99999999:
                            continue
                        result.append(
                            (rw[1],  # showdate
                             rw[2],  # showmonth
                             row_get_showseason(str(rw[1])),  # showseason
                             row_get_showyear(str(rw[1])),  # showyear
                             rw[12],  # moviecode_id
                             row_get_imax(rw[3]),  # IMAX
                             pinfo['id'],  # pid 的id
                             pinfo['ptype'],  # ptype
                             pinfo['pclass'],  # pclass
                             pinfo['pfamily'],  # pfamily
                             rw[4],  # cinema
                             rw[5],  # chain
                             rw[6],  # sheng
                             rw[13],  # city
                             rw[7],  # device
                             rw[0],  # book
                             enum_box['source'][cinfo['source']],  # source
                             enum_box['data_lv'][cinfo['data_level']],  # data_level
                             1,  # scopy
                             ################### key value 分隔 ###################
                             0 if cinfo['source'] == 'zy' else 1,  # source_c
                             1 if cinfo['source'] == 'zy' else 0,  # source_z
                             1 if cinfo['data_level'] == 'day' else 0,  # 账本等级 日
                             1 if cinfo['data_level'] == 'mon' else 0,  # 账本等级 月
                             1 if cinfo['data_level'] == 'scn' else 0,  # 账本等级 下片
                             rw[8],  # shows
                             rw[9],  # audience
                             rw[10],  # revenue
                             rw[8] if rw[7] == DEVICE_OWNED else 0,  # own_shows
                             rw[9] if rw[7] == DEVICE_OWNED else 0,  # own_audience
                             rw[10] if rw[7] == DEVICE_OWNED else 0,  # own_revenue
                             rw[8] if rw[7] == DEVICE_LEASED else 0,  # lease_shows
                             rw[9] if rw[7] == DEVICE_LEASED else 0,  # lease_audience
                             rw[10] if rw[7] == DEVICE_LEASED else 0,  # lease_revenue
                             0,  # zz_shows
                             0,  # zz_audience
                             0,  # zz_revenue
                             rw[11] if rw[7] == DEVICE_OWNED else 0,  # own_hallcount
                             rw[11] if rw[7] == DEVICE_LEASED else 0,  # lease_hallcount
                             0,  # zz_hallcount
                             0,  # keycount
                             0,  # downcount
                             0,  # cam_keycount
                             0,  # cam_downcount
                             0,  # pub_keycount
                             0  # pub_downcount
                             )
                        )

                g_load.write(result)

            for cell in delete_list:  # 将value值变成负数
                cinfo = dict(cell[2])
                pinfo = dict(cell[3])
                with open(cinfo['path']) as cell_data:
                    result = []
                    for rw in cell_data:
                        rw = cell_row_cast(rw)
                        # 旧数据中存在不合法的影院编码
                        if rw[4] > 99999999:
                            continue
                        result.append(
                            (rw[1],  # showdate
                             rw[2],  # showmonth
                             row_get_showseason(str(rw[1])),  # showseason
                             row_get_showyear(str(rw[1])),  # showyear
                             rw[12],  # moviecode_id
                             row_get_imax(rw[3]),  # IMAX
                             pinfo['id'],  # pid 的id
                             pinfo['ptype'],  # ptype
                             pinfo['pclass'],  # pclass
                             pinfo['pfamily'],  # pfamily
                             rw[4],  # cinema
                             rw[5],  # chain
                             rw[6],  # sheng
                             rw[13],  # city
                             rw[7],  # device
                             rw[0],  # book
                             enum_box['source'][cinfo['source']],  # source
                             enum_box['data_lv'][cinfo['data_level']],  # data_level
                             1,  # scopy
                             ################### key value 分隔 ###################
                             -(0 if cinfo['source'] == 'zy' else 1),  # source_c
                             -(1 if cinfo['source'] == 'zy' else 0),  # source_z
                             -1 if cinfo['data_level'] == 'day' else 0,  # 账本等级 日
                             -1 if cinfo['data_level'] == 'mon' else 0,  # 账本等级 月
                             -1 if cinfo['data_level'] == 'scn' else 0,  # 账本等级 下片
                             -rw[8],  # shows
                             -rw[9],  # audience
                             -rw[10],  # revenue
                             -rw[8] if rw[7] == DEVICE_OWNED else 0,  # own_shows
                             -rw[9] if rw[7] == DEVICE_OWNED else 0,  # own_audience
                             -rw[10] if rw[7] == DEVICE_OWNED else 0,  # own_revenue
                             -rw[8] if rw[7] == DEVICE_LEASED else 0,  # lease_shows
                             -rw[9] if rw[7] == DEVICE_LEASED else 0,  # lease_audience
                             -rw[10] if rw[7] == DEVICE_LEASED else 0,  # lease_revenue
                             0,  # zz_shows
                             0,  # zz_audience
                             0,  # zz_revenue
                             -rw[11] if rw[7] == DEVICE_OWNED else 0,  # own_hallcount
                             -rw[11] if rw[7] == DEVICE_LEASED else 0,  # lease_hallcount
                             0,  # zz_hallcount
                             0,  # keycount
                             0,  # downcount
                             0,  # cam_keycount
                             0,  # cam_downcount
                             0,  # pub_keycount
                             0  # pub_downcount
                             )
                        )
                    # group_csv_writer.writerows(result)
                    g_load.write(result)

    @asyncio.coroutine
    def clean_groups(self):
        while (True):
            with self.clean_group_monitor.update():
                files = []
                for f in os.listdir(group_storage_loc):
                    if not f.endswith('json'):
                        continue
                    files.append({
                        'name': os.path.join(group_storage_loc, f),
                        'ctime': os.path.getctime(os.path.join(group_storage_loc, f)),
                        'md5': f.split('.')[0]
                    })

                sorted_files = sorted(files, key=lambda e: e['ctime'], reverse=True)

                for f in sorted_files[5:]:
                    if f['name'].endswith('init.json'):
                        continue
                    self.pub_conn('delete from publish_groups where groups = %s', f['md5'])
                    os.remove(f['name'])

            yield from self.clean_group_monitor.wait()

    def url__touch__project(self, pid=None):

        self.project_monitor.touch()

        return ''

    def url__touch__task(self, tid=None):

        tasktype = 'day'  # select type by tid
        m = getattr(self, tasktype + '_monitor', None)
        if m:
            m.touch()

        return ''

    def url__status(self):
        return


if __name__.startswith('uwsgi_file_'):
    application = App()
    application.init_async_work()
    # uwsgi --asyncio 3 --http-socket :9090 --greenlet --wsgi-file bpm_publish_srv.py
