# generators生成器用法
# with open("C:\Workcode\PL\\txt") as f:
#     for line in f:   # 这个地方迭代文件
#         print(line)
#
# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# # Print all the numbers of the Fibonacci sequence that are lower than 1000
# for i in fibonacci_generator():
#     if i > 1000:
#         break
#     print(i)


a = (x*x for x in range(100))

print(type(a))

print(sum(a))

print(sum(a))

# collections包常见用法

import collections
# print(dir(collections))

from collections import Counter
a = Counter('blue')
b = Counter('yellow')

print(a,'\n', b)
print((a+b).most_common(3))

#字典默认value
from collections import defaultdict
my_dict = defaultdict(lambda : 'default value')
my_dict['a'] = 42

print(my_dict['a'])
print(my_dict['b'])

import itertools
print(dir(itertools))

from itertools import permutations


for p in permutations([1,2,3]):
    print(p)


from itertools import combinations

for c in combinations([1, 2, 3, 4], 2):
    print(c)


from itertools import chain
print(type(chain(range(3), range(12, 15))))
for c in chain(range(3), range(12, 15)):
    print(c)
# packing/unpacking特性

a, *b, c = [2, 7, 5, 6, 3, 4, 1]
print(a)
print(b)
print(c)

def repeat(count, name):
    print(count, name)
    for i in range(count):
        print(name)

print("Call function repeat using a list of arguments:")
args = [4, "cats"]
repeat(*args)

print("Call function repeat using a dictionay of keyword arguments:")
args2 = {'name':'cats', 'count':4,}
repeat(**args2)

def f(*args, **kwargs):
    print("arguments list", args)
    print("keyword arguments", kwargs)

f(3,4,9, foo=42, bar=7)

# Decorators装饰器

# 1，缓存装饰器
# 2，权限验证装饰器
# 3，计时装饰器
# 4，日志装饰器
# 5，路由装饰器
# 6，异常处理装饰器
# 7，错误重试装饰器

def cache(function):
    cached_values = {}
    def wrapping_function(*args):
        if args not in cached_values:
            cached_values[args] = function(*args)
        return cached_values[args]
    return wrapping_function

@cache
def fib(n):
    print('calling fibonacci(%s)' % n)
    if n < 2:
        return n
    return fib(n-1)+fib(n-2)
print([fib(n) for n in range(1, 9)])


from functools import lru_cache

@lru_cache(maxsize=None)
def fibb(n):
    print('nihao %s' % n)
    if n <2:
        return n
    return fibb(n-1)+fibb(n-2)

print([fibb(n) for n in range(1,9)])


# Context Managers上下文管理期

from time import time
class Timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = (time()-self.start)*1000
        print(self.message.format(elapsed_time))

with Timer("Elapsed time to compute some prime numbers: {}ms"):
    primes = []
    for x in range(2, 500):
        if not any(x%p == 0 for p in primes):
            primes.append(x)

    print("primes: {}".format(primes))
