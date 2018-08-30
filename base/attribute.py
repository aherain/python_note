def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


for i in fib():
    if i> 1000:
        break
    print(i)

a = (x*x for x in range(10))
# a = [x*x for x in range(10)]
print(type(a))

print(sum(a))

print(sum(a))

import collections


print(dir(collections))

a = collections.Counter('nihaoherain')
b = collections.Counter('helloword')
print((a+b).most_common(3))

my_dict = collections.defaultdict(lambda: 'default value')
my_dict['a'] = 'nihao'
print(my_dict['a'], my_dict['b'])



import json

def aa():
    return 1000
def tree():
    return collections.defaultdict(tree)
root = tree()
print(type(root['www']), root['www'])
root['Page']['Python']['default']['Title'] = 'Using default'
root['Page']['Python']['default']['Subtitle'] = 'Create a tree'
root['Page']['Java'] = None

print(json.dumps(root, indent=4))


import itertools
print(dir(itertools))

for c in itertools.combinations([1,2,3,4,5],2):
    print(c)

for c in itertools.chain([1,2,3], [8,9,10]):
    print(c)

a, *b, c = [2, 7, 5, 6, 3, 4, 1]

print(a)
print(b)
print(c)

def repeat(count, name):
    for i in range(count):
        print(name)

print("Call function repeat using a list of arguments:")
args = [4, "cats"]
repeat(*args)

print("Call function repeat using a dictionary of keyword arguments:")
args2 = {'count': 4, 'name': 'cats'}
repeat(**args2)
# def cache(function):
#     cached_values = {}
#     def wrapping_function(*args):
#         if args not in cached_values:
#             cached_values[args] = function(*args)
#
#         return cached_values[args]
#     return wrapping_function
#
# @cache
# def fib(n):
#     print('calling fibonacci(%s)' % n)
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
#
# print([fib(n) for n in range(1, 9)])

from time import time
class Timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time()
        return None  # could return anything, to be used like this: with Timer("Message") as value:

    def __exit__(self, type, value, traceback):
        elapsed_time = (time() - self.start) * 1000
        print(self.message.format(elapsed_time))


with Timer("Elapsed time to compute some prime numbers: {}ms"):
    primes = []
    for x in range(2, 500):
        if not any(x % p == 0 for p in primes):
            primes.append(x)
    print("Primes: {}".format(primes))


def use_logging(func):
    print('%s is running' % func.__name__)
    func()

def foo():
    print("I am foo")
use_logging(foo)


def use_log(func):
    def wrapper(name):
        print('%s is running' % func.__name__)
        return func(name)
    return wrapper

# foo = use_log(foo)
# foo()

@use_log
def nihao(name):
    print('nihao is func  [%s]' % name)

nihao('vfvf')



def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                print("%s is running" % func.__name__)
            elif level == "info":
                print("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warn") # @use_logging(level="warn")等价于@decorator
def foo(name='foo'):
    print("i am %s" % name)

foo()


# 类装饰器 __init__ 获取函数  __call__ 回调函数
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')

@Foo
def bar():
    print('bar')
bar()

# 装饰器
def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__)# 输出 'with_logging'
        print(func.__doc__) # 输出 None
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f(x):
   """does some math"""
   return x + x * x
logged(f)

#wraps 复制函数的装饰信息【函数名，doc 信息】
from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__)# 输出 'f'
        print(func.__doc__) # 输出 'does some math'
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math，logged"""
   return x + x * x

print(f(2))

