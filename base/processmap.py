import time
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial

def add(x, y):
    print(datetime.now(), "enter add func")
    time.sleep(2)
    print(datetime.now(), "leave add func")
    return x+y


def add_wrap(args):
    # print(args)
    return add(*args)

if __name__ == "__main__":
    # aa = map(add, [1, 2, 3], [4, 5, 6]) #python 内建的map方法
    # print(list(aa))

    pool = ThreadPool(4)
    print(pool.map(add_wrap, [(1,2),(2,3),(3,4),(4,5), (6,7)]))
    pool.close()
    pool.join()
