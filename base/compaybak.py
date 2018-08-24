def chain_release_compare(self):
    book1, book2, device = self.task_type.split('_')
    moviecodes = self.db.db_fdm('''select pid,lower(code) as moviecode from fdm_moviecode where pid = %s''', self.pid)
    if not moviecodes:
        return {}
    moviecodes_set = set()
    for line in moviecodes:
        moviecodes_set.add(line['moviecode'])

    devicestr = ''
    if self.task_type == '8_7_release':
        devicestr = ' and device=2'

    dvdict = {'0': '全部', '1': '自购', '2': '租赁', '3': '其他'}
    chain_con = '' if int(self.chain.strip()) == 100000 else ' and chain=%s' % self.chain
    dataset = self.db.db_midas(f'''select chain,lower(moviecode) as moviecode, cinema, device,
                        sum( if (book = %s, shows , 0)) as shows1,
                        sum(if(book = %s, shows , 0)) as shows2,
                        sum( if (book = %s, audience , 0)) as audience1,
                        sum(if(book = %s, audience , 0)) as audience2,
                        sum( if (book = %s, revenue , 0)) as revenue1,
                        sum(if(book = %s, revenue , 0)) as revenue2
                        from stt_boxoffice where book in (%s, %s) {chain_con} {devicestr}
                        and moviecode in ("{'","'.join(moviecodes_set)}")
                        group by chain, moviecode, cinema,device
            ''', (int(book1), int(book2),int(book1), int(book2),int(book1), int(book2),int(book1), int(book2)))
    moviecode_set = set()
    cinemacode_set = set()
    # 在这里总票房差值求和
    for res in dataset:
        moviecode_set.add(str(res['moviecode']))
        cinemacode_set.add(str(res['cinema']))

    if not moviecode_set:
        return []
    chains = self.chains
    code_movie = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code, `copy_name` from uni_moviecodes where code in ("{'","'.join(moviecode_set)}") '''))
    cinema_name = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code, `name` from uni_cinemas where code in ("{'","'.join(cinemacode_set)}") '''))
    code_zone = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code,
        (case zone when 0 then '全国' when 1 then '甲区' when 2 then '乙区' when 3 then '其他' else '无' end) as zonename
        from fdm_moviecode where code in ("{'","'.join(moviecode_set)}") '''))

    deal_data = []
    r1 = 0
    r2 = 0
    for line in dataset:
        r1 = r1 + int(line['revenue1'])
        r2 = r2 + int(line['revenue2'])
        deal_data.append({'moviecode': line['moviecode'],
                          'moviename': code_movie.get(line['moviecode'], line['moviecode']),
                          'moviezone': code_zone.get(line['moviecode'], '未知'),
                          'chain': chains.get(line['chain'], line['chain']),
                          'cinemacode': line['cinema'],
                          'cinemaname': cinema_name.get(str(line['cinema']), str(line['cinema'])),
                          'device': dvdict[str(line['device'])],
                          'shows1': str(line['shows1']),
                          'shows2': str(line['shows2']),
                          'shows_diff': str(line['shows1'] - line['shows2']),
                          'audience1': str(line['audience1']),
                          'audience2': str(line['audience2']),
                          'audience_diff': str(line['audience1'] - line['audience2']),
                          'revenue1': str(line['revenue1']),
                          'revenue2': str(line['revenue2']),
                          'revenue_diff': str(line['revenue1'] - line['revenue2'])
                          })
    self.compare_result = r1 - r2
    self.download_chain = deal_data

    return deal_data

def hall_release_compare(self):
    # 精确到影厅和日期
    book1, book2, device = self.task_type.split('_')
    book1 = int(book1)
    book2 = int(book2)
    devicestr = ''
    if self.task_type == '8_7_release':
        devicestr = ' and device=2'
    dvdict = {'0': '全部', '1': '自购', '2': '租赁', '3': '其他'}
    chain_con = '' if self.chain == 100000 else ' and chain=%s' % self.chain
    dataset = self.db.db_midas(f''' select showdate,chain,lower(moviecode) as moviecode,cinema,device, hall,
                    sum( if (book = %s, shows , 0)) as shows1,sum(if(book = %s, shows , 0)) as shows2,
                    sum( if (book = %s, audience , 0)) as audience1,sum(if(book = %s, audience , 0)) as audience2,
                    sum( if (book = %s, revenue , 0)) as revenue1,sum(if(book = %s, revenue , 0)) as revenue2
                    from stt_boxoffice where book in (%s, %s) {chain_con} {devicestr} and moviecode=%s and cinema=%s
                    group by showdate,chain,moviecode,cinema,device,hall
                    ''', (int(book1), int(book2),int(book1), int(book2),int(book1), int(book2),
                          int(book1), int(book2), self.moviecode, self.cinemacode))
    moviecode_set = set()
    cinemacode_set = set()
    # 在这里总票房差值求和
    for res in dataset:
        moviecode_set.add(str(res['moviecode']))
        cinemacode_set.add(str(res['cinema']))

    if not moviecode_set:
        return []
    chains = self.chains
    code_movie = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code, `copy_name` from uni_moviecodes where code in ("{'","'.join(moviecode_set)}") '''))
    cinema_name = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code, `name` from uni_cinemas where code in ("{'","'.join(cinemacode_set)}") '''))
    code_zone = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code,
        (case zone when 0 then '全国' when 1 then '甲区' when 2 then '乙区' when 3 then '其他' else '无' end) as zonename
        from fdm_moviecode where code in ("{'","'.join(moviecode_set)}") '''))
    deal_data = []
    r1, r2 = 0, 0
    for line in dataset:
        r1 = r1 + int(line['revenue1'])
        r2 = r2 + int(line['revenue2'])
        deal_data.append({
                          'showdate': datetime.datetime.strptime(str(line['showdate']),'%Y%m%d').strftime('%Y-%m-%d'),
                          'moviecode': line['moviecode'],
                          'moviename': code_movie.get(line['moviecode'], line['moviecode']),
                          'moviezone': code_zone.get(line['moviecode'],'未知'),
                          'chain': chains.get(line['chain'],line['chain']),
                          'cinemacode': line['cinema'],
                          'cinemaname': cinema_name.get(str(line['cinema']), str(line['cinema'])),
                          'hall': line['hall'],
                          'device': dvdict[str(line['device'])],
                          'shows1': str(line['shows1']),
                          'shows2': str(line['shows2']),
                          'shows_diff': str(line['shows1'] - line['shows2']),
                          'audience1': str(line['audience1']),
                          'audience2': str(line['audience2']),
                          'audience_diff': str(line['audience1'] - line['audience2']),
                          'revenue1': str(line['revenue1']),
                          'revenue2': str(line['revenue2']),
                          'revenue_diff': str(line['revenue1'] - line['revenue2'])
                          })
    self.compare_result = r1 - r2
    self.download_chain = deal_data
    return deal_data

def release_zhuanzi_compare(self):
    moviecodes = self.db.db_fdm('''select pid, lower(code) as moviecode from fdm_moviecode where pid = %s''',self.pid)
    if not moviecodes:
        return {}
    # 组织任务：
    moviecodes_set = set()
    for line in moviecodes:
        moviecodes_set.add(line['moviecode'])

    # 获取院线自购
    chain_selfBuy = self.db.db_midas(f'''select chain,lower(moviecode) as moviecode,cinema,sum(shows) as chain_shows,
            sum(audience) as chain_audience,sum(revenue) as chain_revenue from stt_boxoffice
            where book = 8 and moviecode in ("{'","'.join(moviecodes_set)}") and chain = %s and device=1
            GROUP BY chain,moviecode,cinema''', (self.chain))

    # 获取中影租赁
    zhongying_lease = self.db.db_midas(f'''select chain,lower(moviecode) as moviecode,cinema,
            sum(shows) as zhongying_shows, sum(audience) as zhongying_audience,sum(revenue) as zhongying_revenue
            from stt_boxoffice where book = 7 and moviecode in ("{'","'.join(moviecodes_set)}")
            and chain = %s and device=2 GROUP BY chain,moviecode,cinema''', (self.chain))

    # 获取专资票房
    moviecode_ids = self.db.db_zhuanzi(f'''
            SELECT `id` FROM uni_moviecodes WHERE `code` in ("{'","'.join(moviecodes_set)}")''')
    movieids = [line['id'] for line in moviecode_ids] if moviecode_ids else None
    if movieids:
        zhuanzi_box = self.db.db_zhuanzi(f'''select chain, LOWER (tc.code) as moviecode, cinema,zhuanzi_shows,
                zhuanzi_audience,zhuanzi_revenue from (select chain,lower(moviecode_id) as moviecode,
                cinema,sum(shows) as zhuanzi_shows,sum(audience) as zhuanzi_audience,sum(revenue) as zhuanzi_revenue
                from box_office where  moviecode_id in {self.db.in_clause(movieids)} and chain = {self.chain}
                group by chain, moviecode,cinema) tt left join uni_moviecodes tc on tt.moviecode=tc.id ''', tuple(movieids))
    else:
        zhuanzi_box = []
    # 组装数据：根据moviecode 拿到影片名， chain拿到院线名， cinemacode 获取院线名
    moviecode_set = set()
    cinemacode_set = set()
    key_set = set()
    chain_map = {}
    zhongying_map = {}
    zhuanzi_map = {}
    for line in chain_selfBuy:
        moviecode_set.add(str(line['moviecode']))
        cinemacode_set.add(str(line['cinema']))
        key_str = (str(line['chain']), str(line['cinema']), str(line['moviecode']))
        key_set.add(key_str)
        chain_map[key_str] = line

    for line in zhongying_lease:
        moviecode_set.add(str(line['moviecode']))
        cinemacode_set.add(str(line['cinema']))
        key_str = (str(line['chain']), str(line['cinema']), str(line['moviecode']))
        key_set.add(key_str)
        zhongying_map[key_str] = line

    for line in zhuanzi_box:
        moviecode_set.add(str(line['moviecode']))
        cinemacode_set.add(str(line['cinema']))
        key_str = (str(line['chain']), str(line['cinema']), str(line['moviecode']))
        key_set.add(key_str)
        zhuanzi_map[key_str] = line

    chains = self.chains
    code_movie = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code, `copy_name` from uni_moviecodes where code in ("{'","'.join(moviecode_set)}") '''))
    cinema_name = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code, `name` from uni_cinemas where code in ("{'","'.join(cinemacode_set)}") '''))
    # 过滤不是华夏发行的电影
    fmd_moviecode = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code,  pid from fdm_moviecode where LOWER(code) in  ("{'","'.join(moviecode_set)}") '''
    ))
    code_zone = dict(self.db.db_fdm.tuple(f'''select CONVERT(`code`, CHAR(50)) as code,
        (case zone when 0 then '全国' when 1 then '甲区' when 2 then '乙区' when 3 then '其他' else '无' end) as zonename
        from fdm_moviecode where code in ("{'","'.join(moviecode_set)}") '''))
    # 开始组合票房数据
    dataset = {}
    r1, r2 = 0, 0
    for key in key_set:
        chain, cinema, moviecode = key
        if moviecode not in fmd_moviecode:
            continue
        chain_data = chain_map.get(key, {'chain_shows': 0, 'chain_audience': 0, 'chain_revenue': 0})
        zhongying_data = zhongying_map.get(key,
                                           {'zhongying_shows': 0, 'zhongying_audience': 0, 'zhongying_revenue': 0})
        zhuanzi_data = zhuanzi_map.get(key, {'zhuanzi_shows': 0, 'zhuanzi_audience': 0, 'zhuanzi_revenue': 0})
        r1 = r1 + (chain_data['chain_revenue'] + zhongying_data['zhongying_revenue'])
        r2 = r2 + zhuanzi_data['zhuanzi_revenue']
        dataset[key] = {'moviecode': moviecode,
                        'moviename': code_movie.get(moviecode,moviecode),
                        'moviezone': code_zone.get(moviecode,'未知'),
                        'chainname': chains.get(int(chain), chain),
                        'cinemacode': cinema,
                        'cinemaname': cinema_name.get(cinema, cinema),
                        'device': '全部',
                        'shows_chain': str(chain_data['chain_shows'] + zhongying_data['zhongying_shows']),
                        'shows_zhuanzi': str(zhuanzi_data['zhuanzi_shows']),
                        'shows_chazhi': str((chain_data['chain_shows'] + zhongying_data['zhongying_shows']) -
                                            zhuanzi_data['zhuanzi_shows']),
                        'audience_chain': str(chain_data['chain_audience'] + zhongying_data['zhongying_audience']),
                        'audience_zhuanzi': str(zhuanzi_data['zhuanzi_audience']),
                        'audience_chazhi': str((chain_data['chain_audience'] + zhongying_data['zhongying_audience']) -
                                               zhuanzi_data['zhuanzi_audience']),
                        'revenue_chain': str(chain_data['chain_revenue'] + zhongying_data['zhongying_revenue']),
                        'revenue_zhuanzi': str(zhuanzi_data['zhuanzi_revenue']),
                        'revenue_chazhi': str((chain_data['chain_revenue'] + zhongying_data['zhongying_revenue']) -
                                              zhuanzi_data['zhuanzi_revenue'])}

    self.compare_result = r1 - r2
    return list(dataset.values())

def hall_release_zhuanzi_compare(self):
    # 获取院线自购
    chain_selfBuy = self.db.db_midas('''select showdate,chain,lower(moviecode) as moviecode,cinema,hall,
            sum(shows) as chain_shows,sum(audience) as chain_audience,sum(revenue) as chain_revenue
            from stt_boxoffice where book = 8 and chain = %s and device=1 and lower(moviecode)=%s and cinema = %s
            GROUP BY showdate,chain,moviecode,cinema,hall''', (self.chain, self.moviecode, self.cinemacode))

    # 获取中影租赁
    zhongying_lease = self.db.db_midas('''select showdate,chain,lower(moviecode) as moviecode,cinema,hall,
           sum(shows) as zhongying_shows,sum(audience) as zhongying_audience,sum(revenue) as zhongying_revenue
           from stt_boxoffice where book = 7 and chain = %s and device=2 and lower(moviecode)=%s and cinema = %s
           GROUP BY showdate,chain,moviecode,cinema,hall''', (self.chain, self.moviecode, self.cinemacode))

    # 获取专资票房
    moviecode_ids = self.db.db_zhuanzi('''SELECT `id` FROM uni_moviecodes WHERE `code` = %s''', self.moviecode)
    movieids = [line['id'] for line in moviecode_ids] if moviecode_ids else None
    if movieids:
        zhuanzi_box = self.db.db_zhuanzi('''select show_day as showdate,chain,lower(moviecode_id) as movieid,cinema,
                hall,sum(shows) as zhuanzi_shows,sum(audience) as zhuanzi_audience,sum(revenue) as  zhuanzi_revenue
                from box_office where moviecode_id =%s and cinema=%s group by show_day, chain, moviecode_id,
                cinema,hall ''', (movieids[0], self.cinemacode))
    else:
        zhuanzi_box = []

    # 组装数据：根据moviecode 拿到影片名， chain拿到院线名， cinemacode 获取院线名
    moviecode_set = set()
    cinemacode_set = set()
    key_set = set()

    chain_map = {}
    zhongying_map = {}
    zhuanzi_map = {}

    for line in chain_selfBuy:
        moviecode_set.add(str(line['moviecode']))
        cinemacode_set.add(str(line['cinema']))
        key_str = (str(line['showdate']),str(line['chain']), str(line['cinema']), str(line['moviecode']), str(line['hall']))
        key_set.add(key_str)
        chain_map[key_str] = line

    for line in zhongying_lease:
        moviecode_set.add(str(line['moviecode']))
        cinemacode_set.add(str(line['cinema']))
        key_str = (str(line['showdate']),str(line['chain']), str(line['cinema']), str(line['moviecode']), str(line['hall']))
        key_set.add(key_str)
        zhongying_map[key_str] = line

    for line in zhuanzi_box:
        moviecode_set.add(str(self.moviecode))
        cinemacode_set.add(str(line['cinema']))
        key_str = (str(line['showdate']),str(line['chain']), str(line['cinema']), str(line['moviecode']), str(line['hall']))
        key_set.add(key_str)
        zhuanzi_map[key_str] = line

    chains = self.chains
    code_movie = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code, `copy_name` from uni_moviecodes where LOWER(code) in ("{'","'.join(moviecode_set)}") '''))
    cinema_name = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code, `name` from uni_cinemas where code in ("{'","'.join(cinemacode_set)}") '''))
    code_zone = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code,
        (case zone when 0 then '全国' when 1 then '甲区' when 2 then '乙区' when 3 then '其他' else '无' end) as zonename
        from fdm_moviecode where code in ("{'","'.join(moviecode_set)}") '''))
    # 开始组合票房数据
    dataset = {}
    for key in key_set:
        showdate, chain, cinema, moviecode, hall = key
        chain_data = chain_map.get(key, {'chain_shows': 0, 'chain_audience': 0, 'chain_revenue': 0})
        zhongying_data = zhongying_map.get(key,
                                           {'zhongying_shows': 0, 'zhongying_audience': 0, 'zhongying_revenue': 0})
        zhuanzi_data = zhuanzi_map.get(key, {'zhuanzi_shows': 0, 'zhuanzi_audience': 0, 'zhuanzi_revenue': 0})
        dataset[key] = {'showdate': datetime.datetime.strptime(showdate,'%Y%m%d').strftime('%Y-%m-%d'),
                        'moviecode': moviecode,
                        'moviename': code_movie.get(moviecode,moviecode),
                        'moviezone': code_zone.get(moviecode, '未知'),
                        'chainname': chains.get(int(chain), chain),
                        'cinemacode': cinema,
                        'cinemaname': cinema_name.get(cinema, cinema),
                        'hall': hall,
                        'device': '全部',
                        'shows_chain': str(chain_data['chain_shows'] + zhongying_data['zhongying_shows']),
                        'shows_zhuanzi': str(zhuanzi_data['zhuanzi_shows']),
                        'shows_chazhi': str((chain_data['chain_shows'] + zhongying_data['zhongying_shows']) -
                                            zhuanzi_data['zhuanzi_shows']),
                        'audience_chain': str(chain_data['chain_audience'] + zhongying_data['zhongying_audience']),
                        'audience_zhuanzi': str(zhuanzi_data['zhuanzi_audience']),
                        'audience_chazhi': str(
                            (chain_data['chain_audience'] + zhongying_data['zhongying_audience']) -
                            zhuanzi_data['zhuanzi_audience']),
                        'revenue_chain': str(chain_data['chain_revenue'] + zhongying_data['zhongying_revenue']),
                        'revenue_zhuanzi': str(zhuanzi_data['zhuanzi_revenue']),
                        'revenue_chazhi': str((chain_data['chain_revenue'] + zhongying_data['zhongying_revenue']) -
                                              zhuanzi_data['zhuanzi_revenue']),
                        }
    return list(dataset.values())

def release_chainsSettle_compare(self):
    moviecodes = self.db.db_fdm('''select pid,lower(code) as moviecode, distributions from fdm_moviecode where pid = %s''', self.pid)
    fdm_moviecode, fmd_zf_m = {}, {}
    for line in moviecodes:
        dis = json.loads(line['distributions'])
        if type(dis) is list:
            for fen in dis:
                if line['moviecode'] not in fdm_moviecode:
                    fdm_moviecode[line['moviecode']] = []
                    fmd_zf_m[line['moviecode']] = {'min_date': fen['start_time'],
                                                   'min_ratio': int(fen['huaxia_own']),
                                                   'max_date': fen['end_time'],
                                                   'max_ratio': int(fen['huaxia_own'])
                                                   }
                else:
                    if fmd_zf_m[line['moviecode']]['min_date'] >= fen['start_time']:
                        fmd_zf_m[line['moviecode']]['min_date'] = fen['start_time']
                        fmd_zf_m[line['moviecode']]['min_ratio'] = int(fen['huaxia_own'])

                    if fmd_zf_m[line['moviecode']]['max_date'] < fen['end_time']:
                        fmd_zf_m[line['moviecode']]['max_date'] = fen['end_time']
                        fmd_zf_m[line['moviecode']]['max_ratio'] = int(fen['huaxia_own'])

                fdm_moviecode[line['moviecode']].append({
                    'moviecode': line['moviecode'],
                    'start_date': fen['start_time'],
                    'end_date': fen['end_time'],
                    'ratio': int(fen['huaxia_own'])})
    back_info = {}
    if not moviecodes:
        return back_info
    # 组织任务：
    moviecodes_set = set()
    for line in moviecodes:
        moviecodes_set.add(line['moviecode'])

    chains_st = self.db.db_midas(f'''select chain,showdate,lower(moviecode) as moviecode,sum( shows) as shows,
                                sum( audience) as audience,sum( revenue) as revenue from stt_boxoffice
                                where book =8 and device=1 and chain=%s
                                and lower(moviecode) in ("{'","'.join(moviecodes_set)}")
                                group by chain, showdate, moviecode''', self.chain)
    #给每一天的票房，添加分账比
    chain_movie = {}
    for line in chains_st:
        chain_movie.setdefault((line['chain'], line['moviecode']), []).append({
            'showdate': datetime.datetime.strptime(str(line['showdate']), '%Y%m%d').strftime('%Y-%m-%d'),
            'shows':line['shows'],'audience':line['audience'],'revenue': line['revenue']
        })

    ch_mo_sh_bi = {}
    for key, item in chain_movie.items():
        ch_mo_sh_bi[key] = []
        moviecode = key[1]
        for line in item:
            flag = 1
            if moviecode not in fdm_moviecode:
                continue
            for res in fdm_moviecode[moviecode]:
                if line['showdate'] >= res['start_date'] and line['showdate'] <= res['end_date']:
                    ch_mo_sh_bi[key].append(
                        {'showdate': line['showdate'], 'ratio': res['ratio'],
                         'shows':line['shows'],'audience':line['audience'],'revenue': line['revenue']})
                    flag = 0
            if flag:
                if line['showdate'] < fmd_zf_m[moviecode]['min_date']:
                    ch_mo_sh_bi[key].append(
                        {'showdate': line['showdate'], 'ratio': fmd_zf_m[moviecode]['min_ratio'],
                         'shows':line['shows'],'audience':line['audience'],'revenue': line['revenue']})
                    flag = 0
                if line['showdate'] > fmd_zf_m[moviecode]['max_date']:
                    ch_mo_sh_bi[key].append(
                        {'showdate': line['showdate'], 'ratio': fmd_zf_m[moviecode]['max_ratio'],
                         'shows':line['shows'],'audience':line['audience'],'revenue': line['revenue']})
                    flag = 0

            if flag:
                ch_mo_sh_bi[key].append(
                    {'showdate': line['showdate'], 'ratio':'未知',
                     'shows':line['shows'],'audience':line['audience'],'revenue': line['revenue']})

    dataset = []
    chains = self.chains
    code_movie = dict(self.db.db_fdm.tuple(
        f'''select CONVERT(`code`, CHAR(50)) as code, `copy_name` from uni_moviecodes where code in ("{'","'.join(moviecodes_set)}") '''))

    chains_rec = self.db.db_tatooine('''select unit as chain,moviecode,ratio,sum(shows) as rec_shows,
    sum(audience) as rec_audience,sum(revenue) as rec_revenue from stm_accounts_receivable
    where unit=%s and pid=%s and status=0 group BY unit, moviecode,ratio''', (self.chain, self.pid))

    chains_rec_map = {}
    if chains_rec:
        for line in chains_rec:
            chains_rec_map[(line['chain'],line['moviecode'],line['ratio'])] = {
                                                 'rec_shows': line['rec_shows'],
                                                 'rec_audience': line['rec_audience'],
                                                 'rec_revenue': line['rec_revenue']}
    #对比添加结算待收项
    pending = self.db.db_tatooine('''
                select d.unit, ad.*
                from stm_accounts_late_receivable ad inner join
                ((select id,unit from stm_late_receivable t1 where task is null and status=0)
                UNION
                (select id,t1.unit as unit from stm_late_receivable t1 inner join
                (select unit, task from stm_receivable where type=1 and status=0 and state=0) t2
                on (t1.unit=t2.unit and t1.task=t2.task) where t1.status=0)) d
                on ad.pending_id = d.id where d.unit=%s and ad.pid=%s''', (self.chain, self.pid))

    for line in pending:
        keyt = (line['unit'], line['moviecode'], line['ratio'])
        if keyt not in chains_rec_map:
            chains_rec_map[keyt] = {
                'rec_shows': line['shows'],
                'rec_audience': line['audience'],
                'rec_revenue': line['revenue']}
        else:
            chains_rec_map[keyt]['rec_shows'] = chains_rec_map[keyt]['rec_shows'] + line['shows']
            chains_rec_map[keyt]['rec_audience'] = chains_rec_map[keyt]['rec_audience'] + line['audience']
            chains_rec_map[keyt]['rec_revenue'] = chains_rec_map[keyt]['rec_revenue'] + line['revenue']

    r1, r2 = 0, 0
    chains_stt_map = {}
    for key, item in ch_mo_sh_bi.items():
        chain = key[0]
        moviecode = key[1]
        for line in item:

            chains_stt_map.setdefault((chain,moviecode,line['ratio']), {'min_showdate':0, 'max_showdate':0, 'shows':0, 'audience':0, 'revenue':0})
            sp = chains_stt_map[(chain,moviecode,line['ratio'])]
            if sp['min_showdate']==0 or line['showdate']<sp['min_showdate']:
                sp['min_showdate']=line['showdate']
            if sp['max_showdate']==0 or line['showdate']>sp['max_showdate']:
                sp['max_showdate']=line['showdate']
            sp['shows'] = sp['shows']+line['shows']
            sp['audience'] = sp['audience'] + line['audience']
            sp['revenue'] = sp['revenue'] + line['revenue']
        chains_stt_map[(chain, moviecode, 0)] ={'min_showdate':0, 'max_showdate':0, 'shows':0, 'audience':0, 'revenue':0}

    for key in chains_rec_map:
        chains_stt_map.setdefault(key,{'min_showdate': 0, 'max_showdate': 0, 'shows': 0,'audience': 0, 'revenue': 0})
        chains_stt_map.setdefault((key[0],key[1],0),{'min_showdate': 0, 'max_showdate': 0, 'shows': 0,'audience': 0, 'revenue': 0})

    for k, it in chains_stt_map.items():
        chain, moviecode, ratio = k
        r1 = r1 + it['revenue']
        rec_data =(chains_rec_map[k] if chains_rec_map.get(k, 0) else {
                                                 'rec_shows': 0,
                                                 'rec_audience': 0,
                                                 'rec_revenue': 0})
        r2 = r2 + rec_data['rec_revenue']
        if it['revenue'] == 0:
            it['min_showdate'] = '未知区间'
            it['max_showdate'] = '未知区间'
        if rec_data['rec_audience'] == 0 and it['revenue'] == 0:
            continue
        dataset.append({'moviecode': moviecode,
                        'moviename': code_movie.get(moviecode,moviecode),
                        'chainname': chains.get(int(chain), chain),
                        'showdates': str(it['min_showdate'])+'至'+str(it['max_showdate']),
                        'ratio': ratio,
                        'device': '自购',
                        'stt_shows': str(it['shows']),
                        'rec_shows': str(rec_data['rec_shows']),
                        'diff_shows': str(it['shows']-rec_data['rec_shows']),
                        'stt_audience': str(it['audience']),
                        'rec_audience': str(rec_data['rec_audience']),
                        'diff_audience': str(it['audience']-rec_data['rec_audience']),
                        'stt_revenue': str(it['revenue']),
                        'rec_revenue': str(rec_data['rec_revenue']),
                        'diff_revenue': str(it['revenue']-rec_data['rec_revenue']),
                        })
    self.compare_result = str(r1-r2)
    return dataset

def release_both_confirm(self):
    dataset = []
    moviecodes = self.db.db_fdm('''
            select pid,lower(code) as moviecode,distributions from fdm_moviecode where pid = %s''', self.pid)
    if not moviecodes:
        return {}
    moviecodes_set = set()
    for line in moviecodes:
        moviecodes_set.add(line['moviecode'])

    ch_mo_sh = self.db.db_midas(f'''select chain, showdate,lower(moviecode) as moviecode,sum(revenue) as revenue
    from stt_boxoffice where book=8 and moviecode in  ("{'","'.join(moviecodes_set)}") and device=1
    group by chain, showdate, moviecode''')

    chain_movie = {}
    for line in ch_mo_sh:
        chain_movie.setdefault((line['chain'], line['moviecode']),[]).append(
            {
            'showdate': datetime.datetime.strptime(str(line['showdate']), '%Y%m%d').strftime('%Y-%m-%d'),
            'revenue': line['revenue']
            })
    fdm_moviecode = {}
    fmd_zf_m = {}
    for line in moviecodes:
        if not line['distributions']:
            return []
        dis = json.loads(line['distributions'])
        if type(dis) is list:
            for fen in dis:

                if line['moviecode'] not in fdm_moviecode:
                    fdm_moviecode[line['moviecode']] = []
                    fmd_zf_m[line['moviecode']] = {'min_date': fen['start_time'],
                                                   'min_ratio': int(fen['huaxia_own']),
                                                   'max_date': fen['end_time'],
                                                   'max_ratio': int(fen['huaxia_own'])}
                else:
                     if fmd_zf_m[line['moviecode']]['min_date'] >= fen['start_time']:
                        fmd_zf_m[line['moviecode']]['min_date'] = fen['start_time']
                        fmd_zf_m[line['moviecode']]['min_ratio'] = int(fen['huaxia_own'])

                     if fmd_zf_m[line['moviecode']]['max_date'] < fen['end_time']:
                         fmd_zf_m[line['moviecode']]['max_date'] = fen['end_time']
                         fmd_zf_m[line['moviecode']]['max_ratio'] = int(fen['huaxia_own'])

                fdm_moviecode[line['moviecode']].append({
                    'moviecode': line['moviecode'],
                    'start_date': fen['start_time'],
                    'end_date': fen['end_time'],
                    'ratio': int(fen['huaxia_own'])})
    #统计票房添加分账比
    ch_mo_sh_bi = {}
    for key, item in chain_movie.items():
        ch_mo_sh_bi[key] = []
        moviecode = key[1]
        for line in item:
            flag = True
            if moviecode not in fdm_moviecode:
                continue
            for res in fdm_moviecode[moviecode]:
                if line['showdate'] >= res['start_date'] and line['showdate'] <= res['end_date']:
                    ch_mo_sh_bi[key].append({'showdate': line['showdate'], 'ratio': res['ratio'], 'revenue': line['revenue']})
                    flag = False
            if flag:
                if line['showdate']<fmd_zf_m[moviecode]['min_date']:
                    ch_mo_sh_bi[key].append(
                        {'showdate': line['showdate'], 'ratio': fmd_zf_m[moviecode]['min_ratio'],
                         'revenue': line['revenue']})
                    flag = False
                if line['showdate']>fmd_zf_m[moviecode]['max_date']:
                    ch_mo_sh_bi[key].append(
                        {'showdate': line['showdate'], 'ratio': fmd_zf_m[moviecode]['max_ratio'],
                         'revenue': line['revenue']})
                    flag = False
            if flag:
                ch_mo_sh_bi[key].append(
                    {'showdate': line['showdate'], 'ratio': 99999,'revenue': line['revenue']})
            #添加一个0的分账比票房，让下一步程序扫描到结算票房分账比为0的
            ch_mo_sh_bi[key].append({'showdate': '未知区间', 'ratio': 0,'revenue':0})

    st_ch_mo = self.db.db_tatooine('''select unit as chain,LOWER(moviecode) as moviecode,date_from,date_to,ratio,
            revenue, allocated_revenue as money from stm_accounts_receivable where unit!=100000 and pid = %s
            and status=0''', self.pid)

    sett_arr = []
    for line in st_ch_mo:
        sett_arr.append({
            'datatype': 'settles',
            'chain': line['chain'],
            'moviecode': line['moviecode'],
            'start_date': line['date_from'].strftime('%Y-%m-%d'),
            'end_date': line['date_to'].strftime('%Y-%m-%d'),
            'revenue': line['revenue'],
            'money': line['money'],
            'ratio': int(line['ratio']),
            'is_r': 0
        })

    #添加代收项
    pending = self.db.db_tatooine('''
        select d.unit, ad.*
        from stm_accounts_late_receivable ad inner join
        ((select id,unit from stm_late_receivable t1 where task is null and status=0)
        UNION
        (select id,t1.unit as unit from stm_late_receivable t1 inner join
        (select unit, task from stm_receivable where type=1 and status=0 and state=0) t2
        on (t1.unit=t2.unit and t1.task=t2.task) where t1.status=0)) d
        on ad.pending_id = d.id where ad.pid=%s''', self.pid)
    for line in pending:
        sett_arr.append({
            'datatype': 'settles',
            'chain': line['unit'],
            'moviecode': line['moviecode'],
            'start_date': line['date_from'].strftime('%Y-%m-%d'),
            'end_date': line['date_to'].strftime('%Y-%m-%d'),
            'revenue': line['revenue'],
            'money': line['allocated_revenue'],
            'ratio': int(line['ratio']),
            'is_r':0
        })

    moviecode_team = {}
    for keys, item in ch_mo_sh_bi.items():
        all_list_sort = sorted(item, key=lambda x:x['ratio'])
        moviecode_team[keys] = {}
        start_v = all_list_sort[0]
        #相同的ratio日期为一组
        for res in all_list_sort:
            if start_v['ratio'] == res['ratio']:
                moviecode_team[keys].setdefault(start_v['showdate'],[]).append(res)
            else:
                start_v = res
                if start_v['ratio'] == res['ratio']:
                    moviecode_team[keys].setdefault(start_v['showdate'], []).append(res)

    chains = dict(
        self.db.db_bpm.tuple('select LOWER (CONVERT(`id`, CHAR(50))) as id, `name` from uni_chains where status = 0 and id!=100000'))
    code_movie = dict(self.db.db_fdm.tuple(f'''select LOWER (CONVERT(`code`, CHAR(50))) as code, `copy_name`
                                            from uni_moviecodes where code in ("{'","'.join(moviecodes_set)}") '''))
    is_have_data_chains = set()

    r1, r2 = 0, 0
    for key, tm in moviecode_team.items():
        for k, ret in tm.items():
            min_date = sorted(ret, key=lambda x: x['showdate'])[0]['showdate']
            max_date = sorted(ret, key=lambda x: x['showdate'], reverse=True)[0]['showdate']
            sas_rev, set_rev, set_money, ratio = 0, 0, 0, 0
            for li in ret:
                ratio = int(li['ratio'])
                sas_rev = sas_rev + int(li['revenue'])

            for index, line in enumerate(sett_arr):
                if line['is_r'] == 0 and line['chain'] == key[0] and line['moviecode'] == key[1] and int(line['ratio']) == ratio:
                    if line['ratio'] == 0:
                        min_date = line['date_from']
                        max_date = line['date_to']
                    set_rev = set_rev + line['revenue']
                    set_money = set_money + line['money']
                    sett_arr[index]['is_r']=1
            if int(sas_rev) == 0 and int(set_rev) == 0:
                continue
            is_have_data_chains.add(key[0])
            r1 = r1 + sas_rev
            r2 = r2 + set_rev
            rat = (0 if ratio == 99999 else ratio)
            dataset.append({'chain': chains.get(str(key[0]), str(key[0])),
                            'moviecode': str(key[1]),
                            'moviename':code_movie.get(str(key[1]),str(key[1])),
                            'device': '自购',
                            'fen_bi': str(('未知' if ratio==99999 else ratio/10000)),
                            'date_div': str(min_date) + '至' + str(max_date),
                            'sas_rev': str(sas_rev),
                            'sas_money': str(sas_rev * rat * 0.91737864 / 10000),
                            'set_rev': str(set_rev),
                            'set_money': str(set_money),
                            'rev_chazhi': str(sas_rev - set_rev),
                            'money_chazhi': str(sas_rev * rat / 10000 * 0.91737864 - set_money)
                            })

    not_set_map = {}
    for index, line in enumerate(sett_arr):
        if line['is_r'] == 0:
            r2 = r2 + line['revenue']
            not_set_map.setdefault((line['chain'], line['moviecode'],line['ratio']),{})
            kr = not_set_map[(line['chain'], line['moviecode'],line['ratio'])]
            kr['revenue'] = kr.get('revenue',0) + line['revenue']
            kr['money'] = kr.get('money', 0) + line['money']
            sett_arr[index]['is_r'] = 1

    for k, v in not_set_map.items():
        dataset.append({'chain': chains.get(str(k[0]), str(k[0])),
                        'moviecode': str(k[1]),
                        'moviename': code_movie.get(str(k[1]), str(k[1])),
                        'device': '自购',
                        'fen_bi': str(('未知' if k[2] == 99999 else k[2] / 10000)),
                        'date_div': '未知统计区间',
                        'sas_rev': str(0),
                        'sas_money': str(0),
                        'set_rev': str(v['revenue']),
                        'set_money': str(v['money']),
                        'rev_chazhi': str(-v['revenue']),
                        'money_chazhi': str(-v['money'])
                        })
    for chainid,chainname in chains.items():
        if int(chainid) not in is_have_data_chains:
            flag = 0
            for st in sett_arr:
                if st['chain'] == chainid:
                    flag = 1
                    dataset.append({'chain': chainname,
                                    'moviecode': st['moviecode'],
                                    'moviename': code_movie.get(st['moviecode'],st['moviecode']),
                                    'device': '自购',
                                    'fen_bi': st['ratio'],
                                    'date_div': str(st['start_date']) + '至' + str(st['end_date']),
                                    'sas_rev': 0,
                                    'sas_money': 0,
                                    'set_rev': str(v['revenue']),
                                    'set_money': str(v['money']),
                                    'rev_chazhi': str(-v['revenue']),
                                    'money_chazhi': str(-v['money'])
                                    })

            if not flag:
                dataset.append({'chain': chainname,
                                'moviecode': '无该影片',
                                'moviename': '无该影片',
                                'device': '自购',
                                'fen_bi': 'a/n',
                                'date_div': '无区间',
                                'sas_rev': 0,
                                'sas_money': 0,
                                'set_rev': 0,
                                'set_money': 0,
                                'rev_chazhi': 0,
                                'money_chazhi': 0
                                })

    #中影取整数
    zhongying_mo_sh = self.db.db_midas(f'''
            select chain, showdate, lower(moviecode) as moviecode,
            sum(revenue) as revenue from stt_boxoffice
            where book=7 and moviecode in  ("{'","'.join(moviecodes_set)}") and device=2
            group by chain, showdate, moviecode ''')
    zhongying_movie = {}
    for line in zhongying_mo_sh:
        zhongying_movie.setdefault((line['chain'], line['moviecode']), []).append({
        'showdate': datetime.datetime.strptime(str(line['showdate']), '%Y%m%d').strftime('%Y-%m-%d'),
        'revenue': line['revenue']})

    # 统计中影票房添加分账比
    zy_mo_sh_bi = {}
    for key, item in zhongying_movie.items():
        zy_mo_sh_bi.setdefault(key[1], [])
        moviecode = key[1]
        for line in item:
            flag = True
            for res in fdm_moviecode[moviecode]:
                if line['showdate'] >= res['start_date'] and line['showdate'] <= res['end_date']:
                    zy_mo_sh_bi[key[1]].append(
                        {'showdate': line['showdate'], 'ratio': res['ratio'], 'revenue': line['revenue']})
                    flag = False
            if flag:
                if line['showdate'] < fmd_zf_m[moviecode]['min_date']:
                    zy_mo_sh_bi[key[1]].append(
                        {'showdate': line['showdate'], 'ratio': fmd_zf_m[moviecode]['min_ratio'],
                         'revenue': line['revenue']})
                    flag = False
                if line['showdate'] > fmd_zf_m[moviecode]['max_date']:
                    zy_mo_sh_bi[key[1]].append(
                        {'showdate': line['showdate'], 'ratio': fmd_zf_m[moviecode]['max_ratio'],
                         'revenue': line['revenue']})
                    flag = False
            if flag:
                ch_mo_sh_bi[key].append(
                    {'showdate': line['showdate'], 'ratio': 0,
                     'revenue': line['revenue']})
    # 查找是否下片
    pulled_task_month = self.db.db_tatooine("""
                    select task, month from
                    (select task from stm_accounts_receivable
                    where status=0 and pid=%s
                    GROUP BY task) tr inner join(
                    select id,month from stm_settlement_task
                    where type=3 and status=0) ts on tr.task = ts.id
                    order by task desc """, self.pid)
    if pulled_task_month:
        st_zhongying_mo = self.db.db_tatooine(''' select unit as chain,LOWER(moviecode) as moviecode,
                                date_from, date_to, ratio, revenue, allocated_revenue as money
                                from stm_accounts_receivable where unit=100000 and task=%s
                                and pid = %s and status=0''', (pulled_task_month[0]['task'], self.pid))
    else:
        st_zhongying_mo = self.db.db_tatooine('''select unit as chain,LOWER(moviecode) as moviecode,
                                            date_from, date_to, ratio, revenue, allocated_revenue as money
                                            from stm_accounts_receivable where unit=100000
                                            and pid = %s and status=0''', self.pid)
    sett_arr_zy = []
    for line in st_zhongying_mo:
        sett_arr_zy.append({
            'datatype': 'settles',
            'chain': line['chain'],
            'moviecode': line['moviecode'],
            'start_date': (line['date_from'].strftime('%Y-%m-%d') if line['date_from'] else line['date_from']),
            'end_date':  (line['date_to'].strftime('%Y-%m-%d') if line['date_to'] else line['date_to']),
            'revenue': line['revenue'] if line['revenue'] else int(line['money'])*int((line['ratio'] if line['ratio'] else 4200))/9173.7864,
            'money': line['money'],
            'ratio': int((line['ratio'] if line['ratio'] else 4200))
        })
    for moviecode, item in zy_mo_sh_bi.items():
        min_date = sorted(item, key=lambda x: x['showdate'])[0]['showdate']
        max_date = sorted(item, key=lambda x: x['showdate'], reverse=True)[0]['showdate']
        sas_rev, set_rev, set_money, ratio = 0, 0, 0, 0
        for li in item:
            ratio = int(li['ratio']-100)
            sas_rev = sas_rev + int(li['revenue'])

        for line in sett_arr_zy:
            if line['moviecode'] == moviecode:
                set_rev = set_rev + line['revenue']
                set_money = set_money + line['money']
        r1 = r1 + sas_rev
        r2 = r2 + set_rev
        dataset.append({'chain': '中数发展',
                        'moviecode': moviecode,
                        'moviename': code_movie.get(moviecode, moviecode),
                        'device': '租赁',
                        'fen_bi': str(ratio / 10000),
                        'date_div': str(min_date) + '至' + str(max_date),
                        'sas_rev': str(sas_rev),
                        'sas_money': str(sas_rev * 0.91737864 * ratio / 10000),
                        'set_rev': str(set_rev),
                        'set_money': str(set_money),
                        'rev_chazhi': str(sas_rev-set_rev),
                        'money_chazhi': str(sas_rev * 0.91737864 * ratio / 10000-set_money)
                        })
    self.compare_result = r1-r2
    return dataset

 def js_find_repeat_data_sheet(self, showdate, book, chain, moviecode, cinema):
        # 账本/院线/影片moviecode/ 影院/细化数据到庭
        res = self.db.db_midas('''
        select sheet,showdate,chain,moviecode,cinema,
        sum(shows) as shows,sum(audience) as audience,
        sum(revenue/100) as revenue from stt_boxoffice
        where book=%s and chain=%s and moviecode=%s
        and cinema=%s GROUP BY sheet, showdate, chain, moviecode,
        cinema''', (book, chain, moviecode, cinema))
        return res


#diff.py
from . import DB
from ..constants import *
from .task import Task
class Diff(DB):
    connection = None

    def __init__(self):
        self.connection = self.db_bpm('bpm')

    def get_diff_unit_data(self, unit, compare_date):
        if not isinstance(compare_date, str):
            return

        if len(compare_date) == 6:
            if isinstance(unit, int) and 200000 < unit < 300000:
                self._diff_chain_by_month(unit, compare_date)

            if isinstance(unit, str) and len(unit) == MOVIECODE_LENGTH:
                self._doff_movie_by_month(unit, compare_date)

        elif len(compare_date) == 8:
            if isinstance(unit, int) and 200000 < unit < 300000:
                self._diff_chain_by_day(unit, compare_date)

            if isinstance(unit, str) and len(unit) == MOVIECODE_LENGTH:
                self._doff_movie_by_day(unit, compare_date)

    def _diff_chain_by_month(self, chain, month):
        pass

    def _diff_chain_by_day(self, chain, day):
        pass

    def _doff_movie_by_month(self, moviecode, month):
        pass

    def _doff_movie_by_day(self, moviecode, day):
        pass

    def get_diff_task_data(self, task):
        pass

#剔除users.py
import edb
from . import DB
class Users(DB):
    """只在base_service中用过一次"""
    def find_user_by_name(self, name):
        return self.db_bpm('select * from bpm_users where username = %s', name)

    def find_all_user(self):
        users = self.db_bpm('select `id` ,`realname` from bpm_users')
        userlists = {}
        for line in users:
            userlists[str(line['id'])] = line['realname']

        return userlists

    def find_user_by_department(self, department):
        return self.db_bpm(f'select * from bpm_users where department in {self.in_clause(department)}', department)

#project.py
def get_revenue_zhuanzi_by_moviecode(self, codes):
    return self.db_zhuanzi(f"""select lower(moviecode) as code, sum(revenue) as chain_rev from boxdatas 
                           where book =1 and moviecode in {self.in_clause(codes)} group by moviecode""",codes)
