import re
s = re.match(r'\d{3}-\d{3,8}','000-1234556')
print(s)
print('a  b, c  '.split(' '))
print(re.split(r'[\s\,\t]+','a  b, c  '.strip()))


#re.match() 支持分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0),m.group(1),m.group(2))
print(m.groups())


#编译一次可以多次匹配
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()