import re
# s = re.match(r'\d{3}-\d{3,8}','000-1234556')
# print(s)
# print('a  b, c  '.split(' '))
# print(re.split(r'[\s\,\t]+','a  b, c  '.strip()))


#re.match() 支持分组
m = re.match(r'(?P<id>abc){3}', 'abcabcabc')
print(dir(m))
print(m.group(0))
print(m.groups())

r = re.match(r'(?P<id>\d*)abc(?P=id)', '12abc12')
print(r.group(0))
print(r.groups())

r1 = re.match(r'(\d*)abc\1', '12abc12')

#(?ilmsux)  匹配的侧略
#(?#注释内容不参与匹配)
#(?=后面带有字符的 字符串)
#(?!后面不带xx字符的 字符串)
#(?<=前面带有字符的 字符串)
#(?<!前面不带xx字符的 字符串)

print(r1.group(0))
print(r1.groups())

#编译一次可以多次匹配
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()


#字符 预定义字符集 数量词 边界匹配  逻辑与分组 特殊构造
