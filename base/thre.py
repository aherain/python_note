import requests
import json

# http://192.168.1.211:9095/send_msg?task_type=1&pid=GF2017116&cooperator_id=8&issue_id=23&push_msg=%27你好測試%27

# r = requests.post('http://httpbin.org/post', data = {'key':'value'})

def push_msg(kwargs):
    r = requests.post('http://192.168.1.211:9096/send_msg', data=kwargs)
    # r = requests.get('http://192.168.1.211:9096/send_msg?task_type=1&pid=GF2017116&cooperator_id=8&issue_id=23&push_msg=%27你好測試%27')
    print('请求返回结果', r.text)
    back_data = json.loads(r.text)
    print(back_data['result'])
    return back_data['result']



# push_msg({'task_type': 2, 'pid': 'GF2017116', 'name': '闺蜜2', 'cooperator_id': 1,
#           'push_msg': '该消息为测试标题功能的消息，请忽略',
#           'push_title': 'aa' if None else ''})

#
# r = requests.post('http://192.168.1.211:9095/confirm_project', data={'pid': None })
# print('请果', r.text)
# back_data = json.loads(r.text)
# print(back_data['result'])

# 'http://10.120.1.22:12018/inner/secondary/use_settlement?ids=[1,2]

#线下
r = requests.post('http://192.168.1.211:9095/secondary_issettlement', data={'data': ['hahaha']})
back_data = json.loads(r.text)
print(back_data)
# print(back_data['result'])


#  fdm_new:
# 110     host: 10.120.1.32
# 111     user: php
# 112     passwd: MySQL8.huayingjuhe.com
# 113     port: 3307
# 114     db: fdm


# curl --location-trusted -utatooine2:tatooine2.Midas.W6.huayingjuhe.com -T /data3/bpm/tongji_files/056/056013/data.csv
# "http://127.0.0.1:8030/api/Bestine/stt_boxoffice/_load?label=20181210sheet056013&column_separator=,"


#read uncommitted 事物未提交读，会出现脏读
#read committed   事物提交读，会出现不可重复读
#repeatable read  可重复读， 会遇到幻读
# 幻读是指，在一个事务中，第一次查询某条记录，发现没有，但是，当试图更新这条不存在的记录时，竟然能成功，并且，再次读取同一条记录，它就神奇地出现了。
#Serializable 可串行化,严格的隔离级别,脏读、不可重复读、幻读都不会出现。性能下降



