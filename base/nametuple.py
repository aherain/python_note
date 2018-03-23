from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')

big_yellow = Animal(name='big_yy', age=3, type='dog')

print(big_yellow)
print(big_yellow.name)
print(big_yellow[0])
print(big_yellow._asdict()['name'])

from collections import defaultdict
words = ['hello', 'world', 'nice', 'world']
#使用lambda来定义简单的函数
counter = defaultdict(lambda: 0)
for kw in words:
    counter[kw] += 1
print(counter)