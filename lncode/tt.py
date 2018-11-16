str = "this is really a string example....wow!!!"
substr = "is"

print(str.rfind(substr))
print(str.rfind(substr, 0, 10))
print(str.rfind(substr, 10, 0))

print(str.find(substr))
print(str.find(substr, 0, 10))
print(str.find(substr, 10, 0))




import datetime
a = ('GF2018067', '001105832018', '1', 4300, 95, 1959, 5906200, 295310, 192668, 300, 5418222, datetime.date(2018, 6, 1), datetime.date(2018, 8, 31), 2329835)

b= ('GF2018067', '001105832018', '1', 4300, 95, 1959, 5906200, 295310, 192668, 300, 5418222, datetime.date(2018, 6, 1), datetime.date(2018, 8, 31), 2329835)

print('元组比较',a==b)
