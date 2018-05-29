from multiprocessing import Process, Queue
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
    print('print ',q)


def read(q):
    print('Process %s' % os.getpid())
    while True:
        v = q.get(True)
        print("GET %s from Write Queue"% v)

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

    #用线程池的方式批量创建多个子进程
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,)) #设置每一个进程执行的函数和参数

    print('waiting for all subprocess done...')
    p.close()
    p.join()
    print("all subprocess done")

    # python进程通信，提供了 队列（Queue）,通道（Pipes）等多种方式
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()

    pw.join()
    pr.terminate() #强行终止死循环程序










