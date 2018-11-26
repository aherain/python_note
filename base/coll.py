# '''
# nametuple() 生成可以使用名字来访问元素内容的tuple子类
# deque 双端队列，可以快速的从另外一侧追加和推出对象
# Counter 计数器，主要用来计数
# OrderDict 有序字典
# defaultdict 带有默认值的字典
# '''

from collections import namedtuple
websites = [
    ('Sohu', 'http://www.sohu.com/', '张朝阳'),
    ('Sina', 'http://www.sina.com.cn', '王志东'),
    ('163', 'http://www.163.com/', '丁磊')
]

#创建 将元组数据 namedtuple 化，方便数据的访问
Website = namedtuple('Website', ['name', 'url', 'founder'])
for website in websites:
    website = Website._make(website)
    print(website.url)


import sys
import time
from collections import deque
fancy_loading = deque('>------------')
# while True:
#     print('\r%s' % ''.join(fancy_loading))
#     fancy_loading.rotate(1)
#     sys.stdout.flush()
#     time.sleep(1)

from collections import Counter
s = 'nihao 2018 zhu ni hao yun'
c = Counter(s)
print(c.most_common(5)) #获取出现频率最高的5个字符


from collections import OrderedDict

items = (
    ('a', 1),
    ('b', 2),
    ('c', 3)
)

items = [('a', 1), ('b', 2), ('c', 3)]
regular_dict = dict(items) #元组中的二维元组也可以转成普通的字典

ordered_dict = OrderedDict(items)

print('将元组转成二维数组', ordered_dict)
print('Regular Dict:')
for k, v in regular_dict.items():
    print(k, v)

print('Ordered Dict')
for k, v in ordered_dict.items():
    print(k, v)

from collections import defaultdict

members = [
    ['male', 'john'],
    ['male', 'jack'],
    ['female', 'lily'],
    ['male', 'pony'],
    ['female', 'lucy']
]

result = defaultdict(list)

for sex, name in members:
    result[sex].append(name)

print(result)
print(result['nihao'])

def repeat(count, name):
    for i in range(count):
        print(name)

print("Call function repeat using a list of arguments:")
args = [4, "cats"]
repeat(*args)

print("Call function repeat using a dictionary of keyword arguments:")
args2 = {'count': 4, 'name': 'cats'}
repeat(**args2) #调用方法的传参方式

# def nihao(kwargs):
#     print(kwargs)
#
# nihao({'nihao':121, 'name':'测试'}) #错误的方法


