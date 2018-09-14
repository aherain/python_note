import time
import multiprocessing #每一个单独的进程赋予单独的python解释器（GIL）

def profile(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('COST: {}'.format(end - start))

    return wrapper

def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

@profile
def nomutilprocess():
    fib(35)
    fib(35)


@profile
def hasmutilprocess():
    jobs = []

    for i in range(2):
        p = multiprocessing.Process(target=fib, args=(35,))
        p.start()
        jobs.append(p)

    for p in jobs:
        p.join()


from multiprocessing import Pool
from multiprocessing.dummy import Pool #dummy 是模仿的意思
pool = Pool(2)
pool.map(fib, [35]*2)

from multiprocessing import Process, Pipe

def f(conn):
    conn.send(['hello'])
    conn.close()

parent_conn, child_conn = Pipe()
p = Process(target=f, args=(child_conn,))
p.start()
print(parent_conn.recv())
p.join()

if __name__ == '__main__':
    pass
    # nomutilprocess()
    # hasmutilprocess()