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