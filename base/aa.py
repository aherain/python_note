
# a = [1,3,4,5]
# print(a[::-1])
# print(a.reverse())
# print(a)
# b = (1,3,2)
# print(b[::-1])

tmpstr = 'nihao 12 nihao'
print(tmpstr.replace('nihao', 'we', -1)) #全部替换
import re
rex = r'(ni|hao)'
print(re.sub(rex, 'w1', tmpstr))

my_dict = {'a': 1223, 'b': {'a': 21, 'c': 34}, 'c': 90}
print(map(my_dict.pop, 'a'))
print('删除多个KEY', my_dict)
print(my_dict.pop('a'))
print(my_dict)

import re
rex = r'(ni|nihao)'
print(re.sub(rex, 'w1', tmpstr))
re.sub(rex, 'w1', tmpstr)

