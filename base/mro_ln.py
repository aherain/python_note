class D(object):
    def foo(self):
        print("class D")

class B(D):
    pass

class C(D):
    def foo(self):
        print("class C")

class A(B, C):
    pass

f = A()
#
# A : B C
# C: D
# B: D
# D: object


#a b c d object 继承object的对象都是新式类，新式类遵循广度优先

#如果是旧式对象，执行的对象序列： a b d c d, 出现父类多次执行的情况， 旧式对象遵循深度优先

# 事实上，super 和父类没有实质性的关联。
# super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类。


#函数式编程： filter map reduce
b = filter(lambda x : x>5 , [12,343,45,5,6,1,0])
print(list(b))
b = map(lambda x: x*2, [2]*32)
print(list(b))
from functools import reduce
b = reduce(lambda x,y: x*y, [2]*32)/1024/1024/1024 #2的32次等于 4GB
print(b)
# b= reduce(lambda x, y: x+y, [1,2,3,4,5])


#租房首先考虑 地段
# 立水桥， 立水桥南， 大屯路，关庄， 安立路，北沙滩
# 奥林匹克公园， 奥体中心，安华桥，北土城， 永泰庄，林萃桥， 太阳宫
# 线路：5 8 13 15 10 北京东北地区
#
# 招租：回龙观东大街（地铁站）和谐家园一区，次卧2000元/月，10平左右，押一付三（水电气根据账单均摊），
# 家用设施完备（冰箱，空调，洗衣机，厨房用具），小区坏境整洁，安静宜居，要求室友:不抽烟，不闹腾，不养宠物，
# 有意愿，可以私信我