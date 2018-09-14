class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1
s = MyClass()
print(s.a)
def print_directory_contents(spath):
    import os
    for child in os.listdir(spath):
        scpath = os.path.join(spath, child)
        if os.path.isdir(scpath):
            print_directory_contents(scpath)
        else:
            print(scpath, '\n')

a0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
print(a0)
a1 = range(10)
print(a1)
a2= [i for i in a1 if i in a0]
print(a2)

a3=[a0[s] for s in a0]
print(a3)

a4 = [i for i in a1 if i in a3]
print(a4)

a5 = {i: i*i for i in a1}
print(a5)
a6 = [[i, i*i] for i in a1]
print(a6)


def f(x, l=[]):
    for i in range(x):
        l.append(i*i)

    print(l)

# f(2)  #0,1
# f(3, [3,2,1]) #[3,2,1,0,1,4]
# f(3) #[0,1,0,1,4]
# #
# a
# a b
# a c
# b c d = a b c d #有重复的类不添加该类
# b c e = a b c  #有重复的类不添加该类


def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]

import random
import cProfile
lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')


class A(object):
    def show(self):
        print('base show')

class B(A):
    def show(self):
        print('self show')

obj = B()
obj.show()

obj.__class__ = A
obj.show()


class C(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print('a=', self.__a, 'b=', self.__b)

    def __call__(self, num):
        print('call ', sum([num, self.__a]))

c1 = C(10, 20)
c1.myprint()

c1(80)


class D(object):
    def fn(self):
        print('D fn')

    def __init__(self):
        print('B INIT')

class E(object):
    def fn(self):
        print('E fn')

    def __new__(cls, a):
        print('NEW', a)
        if a > 10:
            return super(E, cls).__new__(cls)
        return D()

    def __init__(self, a):
        print('INIT', a)

d1 = E(5)
d1.fn()

d2 = E(20)
d2.fn()

class F(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print('init')

    def mydefault(self, *args):
        print('default: ' + str(args[0]))

    def __getattr__(self, name):
        print("other fn:", name)
        return self.mydefault

f1 = F(10, 20)
f1.fn1(33)
f1.fn2('hello')
f1.fn3(10)



def mulby(num):
    def gn(val):
        return num*val

    return gn

zw = mulby(7)
print(zw(9))

D = {'a': 1, 'b': 2, 'c': 3}
print(D.items())

for cell in D.items():
    print(cell)

# Removed dict.iteritems(), dict.iterkeys(), and dict.itervalues().
# Instead: use dict.items(), dict.keys(), and dict.values() respectively.
# for k, v in D.iteritems():
#     print(k, v)

def fibs(x):
    result = [0, 1]
    for index in range(x-2):
        result.append(result[-2]+result[-1])
    return result

print(fibs(5))

#python 简洁 明了 严谨 灵活
# if __name__ == '__main__':
#     print_directory_contents('c:\workcode\PL\\base')


