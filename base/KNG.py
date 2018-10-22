Python 零碎见真知

1,切片类型的数据，data[::-1] 实现数据的反转

2,re.sub(pattern,repl,string,count,flags) 其中参数repl可以是固定字符串或者函数名
#快捷反转元音字母【aeiou】
import re
s = 'hello'
vowels = re.findall('(?i)[aeiou]', s)
re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

3, 多层字典的默认结构
import collections,json
def tree():
    return collections.defaultdict(tree)
root = tree()
root['Page']['Python']['default']['Title'] = 'Using default'
root['Page']['Python']['default']['Subtitle'] = 'Create a tree'
root['Page']['Java'] = None
print(json.dumps(root, indent=4))

4, 列表的元素组合，拼接
import itertools
for c in itertools.combinations([1,2,3,4,5],2): #两两组合
    print('combinations', c)
for c in itertools.chain([1,2,3], [8,9,10]): #拼接
    print('chain', c)

5, 通过类的魔法方法:__enter__,__exit__实现计时器
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
    for x in range(2, 500): #找素数最快的方法，用any排除法，埃拉托斯特尼 筛选法
        if not any(x % p == 0 for p in primes):
            primes.append(x)
    print("Primes: {}".format(primes))

6, nametuple() 生成可以使用名字来访问元素内容的tuple子类
from collections import namedtuple
websites = [
    ('Sohu', 'http://www.sohu.com/', '张朝阳'),
    ('Sina', 'http://www.sina.com.cn', '王志东'),
    ('163', 'http://www.163.com/', '丁磊')]
Website = namedtuple('Website', ['name', 'url', 'founder'])
for website in websites:
    website = Website._make(website)
    print(website.url)

7, cProfile对方法实现性能检测
import random
import cProfile
lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')

8, heapq动态堆化,实现优先级队列
import heapq
x = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(x)
heapq.heapify(heap)
print(heapq.heappop(heap))
print(heap) #每次通过heappop取出最小值，然后动态堆化heap

#优先级队列 priority queue
class PriorityQueue(object):
    def __init__(self):
        self._queue = []  # 创建一个空列表用于存放队列
        self._index = 0  # 指针用于记录push的次序

    def push(self, item, priority):
        """队列由（priority, index, item)形式的元祖构成"""
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # 返回拥有最高优先级的项

class Item(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item: {!r}'.format(self.name)

if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 5)
    q.push(Item('bar'), 1)
    q.push(Item('spam'), 3)
    q.push(Item('grok'), 1)
    for i in range(4):
        print(q._queue)
        print(q.pop())


9, 方法，类方法，静态方法的区别
class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)" % (self,x))

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)" % (cls,x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"% x)

a=A()
a.foo('normal function')

a.class_foo('class method')
A.class_foo('ddd')
A.static_foo('vvvv')
A.foo('bbb')
a.static_foo('static method')


10,MRO：Method Resolution Order，即方法解析顺序
#a b c d object 继承object的对象都是新式类，新式类遵循广度优先
#如果是旧式对象，执行的对象序列： a b d c d, 出现父类多次执行的情况， 旧式对象遵循深度优先
# 事实上，super 和父类没有实质性的关联。
# super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类。
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


11, python的多进程实例
from multiprocessing import Process, Queue, Pipe
from multiprocessing import Pool
import os, time, random

# print('Process (%s) is Start' % os.getpid())
#
# pid = os.fork() #windows 系统不支持fork()来创建子进程
#
# if pid == 0:
#     print("child Process (%s), parent Process (%s)" % (os.getpid(), os.getppid()))
# else:
#     print("(%s) just created a child process (%s)" % (os.getpid(), pid))

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

def long_time_task(name):
    print('Run task %s (%s)'%(name, os.getpid()))
    time.sleep(4)

def write(q):
    print('Process %s' % os.getpid())
    for v in ['A', 'B', 'C']:
        q.put(v)
        time.sleep(random.random())
    print('print ', q)


def read(q):
    print('Process %s' % os.getpid())
    while True:
        v = q.get(True)
        print("GET %s from Write Queue"% v)

#管道通信
def f(conn):
    conn.send([42, None, 'hello'])
    while True:
        print('子工道',conn.recv())
if __name__=='__main__':
    # print('Parent process %s.' % os.getpid())
    # p = Process(target=run_proc, args=('test',))
    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')
    p = Process(target=run_proc, args=('test',))
    p.start()
    p.join()
    print('child process is end')
    #
    # #用线程池的方式批量创建多个子进程
    # p = Pool(4)
    # for i in range(5):
    #     p.apply_async(long_time_task, args=(i,)) #设置每一个进程执行的函数和参数
    #
    # print('waiting for all subprocess done...')
    # p.close()
    # p.join()
    # print("all subprocess done")

    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))

    p.close() #关闭进程池
    p.join() #执行进程连接
    print("all subprocess done")
    # # python进程通信，提供了 队列（Queue）,通道（Pipes）等多种方式
    # q = Queue()
    # pw = Process(target=write, args=(q,))
    # pr = Process(target=read, args=(q,))
    # pw.start()
    # pr.start()
    # pw.join()
    # pr.terminate() #强行终止死循环程序

    #通过管道实现进程之间的通信
    parent_conn, child_conn = Pipe()
    pp = Process(target=f, args=(child_conn,))
    pp.start()

    print('双工道', parent_conn.recv())
    parent_conn.send('6666')


12, python 多线程实例
import time, threading
def loop():
    print("thread %s is running.." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s  >>> %s'% (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name) #标记当前线程执行结束

print('thread %s is running...'% threading.current_thread().name)

t = threading.Thread(target=loop,name='LoopThread') #如果线程不命名会有默认的名字
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name) #标记主线程调用结束


#多线程操作共同的变量，为了保证结果预期，需要添加线程锁
balance = 0
lock = threading.Lock()
def change_int(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_int(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join() #start 和 join顺序影响操作吗？

print(balance)


#线程通过全局变量实现数据的通信
L1 = [1, 2, 3]

def add(a, b):
    global L1
    L1 += range(a, b)
    print(L1)

if __name__ == '__main__':
    p1 = threading.Thread(target=add, args=(20, 30))
    p2 = threading.Thread(target=add, args=(30, 40))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print (L1)


from multiprocessing import Process, Manager
def func(dt, lt):
    for i in range(10):
        key = 'arg' + str(i)
        dt[key] = i * i

    lt += range(11, 16)

if __name__ == "__main__":
    manager = Manager()
    dt = manager.dict()
    lt = manager.list()

    p = Process(target=func, args=(dt, lt))
    p.start()
    p.join()
    print(dt, '\n', lt)


13, 正则表达
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


14, requests的方法实例
import requests
# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}
resp = requests.post(url, data=parms, headers=headers)
# Decoded text returned by the request
text = resp.text

url = 'http://httpbin.org/post'
files = {'file': ('data.csv', open('data.csv', 'rb'))}
r = requests.post(url, files=files)