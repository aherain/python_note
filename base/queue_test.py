import sys
is_py2 = sys.version[0] == '2'
if is_py2:
    import Queue as queue
else:
    import queue as queue
q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())

lifo = queue.LifoQueue() #后进先出的队列
for i in range(5):
    lifo.put(i)

while not lifo.empty():
    print(lifo.get())
print('')

import threading
a = 0
class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)

        return

    def __lt__(self, other):
        print('pro', self.priority, other.priority)
        return self.priority < other.priority

    def __iadd__(self, other):
        print('other')
        return 0

    # def __le__(self, other):
    #     return self.priority < other.priority

q = queue.PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))
q.put(Job(2, '2 level job'))
q.put(Job(1, '4 level job'))


# New job: Mid-level job  3
# New job: Low-level job 10
# pro 10 3                  #3 10
# New job: Important job 1
# pro 1 3                   #1 3 10
# New job: 2 level job 2
# pro 2 10
# pro 2 1
# New job: 4 level job 1
# pro 1 2
# pro 1 1



# def process_job(q):
#     while True:
#         next_job = q.get()
#         print('Processing job:', next_job.description)
#         q.task_done()
#
#
# workers = [threading.Thread(target=process_job, args=(q,)),
#            threading.Thread(target=process_job, args=(q,)),
#            ]
#
# for w in workers:
#     w.setDaemon(True)
#     w.start()
#
# q.join()