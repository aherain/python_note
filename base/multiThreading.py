import time, threading

def loop():
    print("thread %s is running.." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s  >>> %s'% (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

print('thread %s is running...'% threading.current_thread().name)

t = threading.Thread(target=loop,name='LoopThread') #如果线程不命名会有默认的名字
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)




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
t2.join()
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