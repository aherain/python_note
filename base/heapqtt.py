import heapq
import random

mylist = list(random.sample(range(100), 10))
print(mylist)

k = 3
largest = heapq.nlargest(k, mylist)
print('最大的前3位', largest)
smallest = heapq.nsmallest(k, mylist)
print('最小的前3位', smallest)

#对原的数组进行堆化

heapq.heapify(mylist)
print('堆化后的列表',mylist)

heapq.heappush(mylist, 105)
print('向堆里添加元素', mylist)
heapq.heappop(mylist)
print('取出堆元素', mylist)

heapq.heappushpop(mylist, 130)

print('添加元素顺便取', mylist)

heapq.heapreplace(mylist, 2)
print('取出元素，顺便添加', mylist)

from functools import reduce
a = reduce(lambda x,y: x*y, [1, 3, 5, 7, 9])
print(a)


#最大字数列的乘积
def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ns = nums[0]
    for m in nums[1:]:
        print(ns * m)
        ns = max(ns * m, m)
    return ns

nums = [2, 3, -2, 4]
maxProduct(nums)