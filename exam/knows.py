from io import StringIO


f = StringIO()
a = f.write('nihao')
print(a)
b = f.write(' 2019')
print(b)

print(f.getvalue())


t = StringIO('Hello!\nHi!\nGoodbye')
while True:
    s = t.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())

import pickle
d = dict(name='Bob', age=20, score=88)
ss = pickle.dumps(d)
print(ss)
# project_list

# 时间序列预测