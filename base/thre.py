import requests
import json

# http://192.168.1.211:9095/send_msg?task_type=1&pid=GF2017116&cooperator_id=8&issue_id=23&push_msg=%27你好測試%27

# r = requests.post('http://httpbin.org/post', data = {'key':'value'})

# def push_msg(kwargs):
#     r = requests.post('http://192.168.1.211:9096/send_msg', data=kwargs)
#     # r = requests.get('http://192.168.1.211:9095/send_msg?task_type=1&pid=GF2017116&cooperator_id=8&issue_id=23&push_msg=%27你好測試%27')
#     print('请求返回结果', r.text)
#     back_data = json.loads(r.text)
#     print(back_data['result'])
#     return back_data['result']
#
#
# push_msg({'task_type': 1, 'pid': 'GF2017116', 'name': '闺蜜2', 'cooperator_id': 8,
#           'push_msg': '《闺蜜2》本月与贵司可结算分帐款金额1,212,190.00元，请与我司联系收款相关事宜'})

cn = {}
test_list=['123','456','789']
cn =cn.fromkeys(test_list,'abc')
print(cn)

