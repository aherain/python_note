import heapq

x = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(x)

heapq.heapify(heap)

print(heapq.heappop(heap))
print(heap) #每次通过heappop取出最小值，然后动态堆化heap

#优先级队列 priority queue


import heapq
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