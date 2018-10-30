alist = [23,54,6,787,88,1,-1, 29]
# def bubbleSort(ls):
#     exchanges = True
#     for i in range(len(ls)-1,0,-1):
#         if exchanges:
#             exchanges = False
#             for j in range(i):
#                 if ls[j] > ls[j+1]:
#                     exchanges = True
#                     temp = ls[j]
#                     ls[j] = ls[j+1]
#                     ls[j+1] = temp

def bubbleSort(ls):
    exchanges = True
    for i in range(len(ls)-1, 0, -1):
        if exchanges:
            exchanges = False
            for j in range(i):
                if ls[j]>ls[j+1]:
                    exchanges = True
                    temp = ls[j]
                    ls[j] = ls[j+1]
                    ls[j+1] = temp

# bubbleSort(alist)#冒泡排序与短冒泡排序
# print('冒泡排序与短冒泡排序的结果', alist)

# def selectSort(ls):
#     for lt in range(len(ls)-1,0,-1):
#         positionOfMax = 0
#         for it in range(1,lt+1):
#             if ls[it]>ls[positionOfMax]:
#                 positionOfMax = it
#
#         temp = ls[lt]
#         ls[lt] = ls[positionOfMax]
#         ls[positionOfMax] = temp

def selectSort(ls):
    for lt in range(len(ls)-1, 0, -1):
        positionOfMax = 0
        #找到列表中最大的值
        for it in range(0, lt+1):
            if ls[it]>ls[positionOfMax]:
                positionOfMax = it
        #把他交换到未排序的最后位置
        temp = ls[lt]
        ls[lt] = ls[positionOfMax]
        ls[positionOfMax] = temp
# selectSort(alist) #两个循环遍历 每次找到最大的放在数组的最后面
# print('选择排序的结果:', alist)

# def insertSort(ls):
#     for i in range(1,len(ls)):
#         pos = i
#         val = ls[i]
#         while pos > 0 and ls[pos-1]>val:
#             ls[pos] = ls[pos-1]
#             pos = pos-1
#         ls[pos] = val

#插入排序，顾名思义找到一个数的应有位置，然后插入进去
def insertSort(ls):
    for i in range(1, len(ls)):
        pos, val = i, ls[i]
        while pos > 0 and ls[pos-1] > val:
            ls[pos] = ls[pos-1]
            pos = pos - 1  # 从第二个值开始到最后一个值，拿一个数值， 然后在前面的有序部分找位置插入进去
        ls[pos] = val
# insertSort(alist)
# print('插入排序的结果:', alist)

#希尔排序就是分 gap 的插入排序, 分间隔的插入排序，每一次插入排序是数组渐变成有序数组
# def shellSort(ls):
#     n = len(ls)
#     gap = n//2
#     while gap > 0:
#         #gap =1 就是普通的插入排序
#         for i in range(gap, n):
#             temp, j = ls[i], i
#             while j>=gap and ls[j-gap] > temp:
#                 ls[j] = ls[j-gap]
#                 j = j-gap
#             ls[j] = temp
#         #普通的插入排序
#         gap = gap //2

# def shellSort(ls):
#     n, gap = len(ls), len(ls)//2
#     while gap > 0:
#         for i in range(gap, n):
#             temp, j = ls[i], i
#             while j >= gap and ls[j-gap] > temp:
#                 ls[j], j = ls[j-gap], j - gap
#                 # j = j - gap
#             ls[j] = temp
#         gap = gap // 2


def shellSort(ls):
    n, gap = len(ls), len(ls)//2
    while gap > 0:
        for i in range(gap, n):
            temp, j = ls[i], i
            while j >= gap and ls[j-gap] > temp:
                ls[j], j = ls[j-gap], j - gap
            ls[j] = temp
        gap = gap // 2


# shellSort(alist)
# print('希尔排序的结果', alist)
from collections import deque
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    def merge(left, right):
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)
        print('合并后的数组', merged)
        return merged
    middle = int(len(lst) // 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

# merge_sort(alist)
# print("归并排序的结果", merge_sort(alist))

#快速排序
# def quicksort(lst, lo, hi):
#     if lo < hi:
#         p = partition(lst, lo, hi)
#         quicksort(lst, lo, p)
#         quicksort(lst, p+1, hi)
#     return
#
# def partition(lst, lo, hi):
#     pivot = lst[hi-1]
#     i = lo - 1
#     for j in range(lo, hi):
#         if lst[j] < pivot:
#             i += 1
#             lst[i], lst[j] = lst[j], lst[i]
#     if lst[hi-1] < lst[i+1]:
#         lst[i+1], lst[hi-1] = lst[hi-1], lst[i+1]
#     return i+1
# quicksort(alist, 0, len(alist))
#Talj is cheap, show the code
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    less, greater = [], []
    base = nums.pop()
    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less) + [base] + quicksort(greater)
# nums = [6, 1,2,7,9,3,4,5,-1,8]
# print('打印快速排序的结果：', quicksort(nums))


# coding:utf-8
# 找零钱问题算法实现：基本版性能分析

# 统计递归次数
recursion_num = 0
# 4种硬币面值
values = [1,5,10,25]
# 缓存数组，为一个一维数组，用于缓存每次递归函数求得的值
# cache[i]表示凑够i美分所需的最少硬币个数，cache的元素都被初始化为-1，表示个数未知
cache = []
# 初始化缓存数组
def init(amount):
    global cache
    cache = [-1] * (amount + 1)

# 凑够amount这么多钱数需要的最少硬币个数
def minCoins(amount):
    global recursion_num
    global cache
    # 需要的最少硬币个数
    ret_min = amount
    # 如果缓存数组中有对应的值，那么直接从中取，不再重复计算了
    if cache[amount] != -1:
        ret_min = cache[amount]
    elif amount < 1:
        ret_min = 0
    # 如果要找的钱数恰好是某种硬币的面值，那么最少只需一个硬币
    elif amount in values:
        ret_min = 1
    else:
        # 遍历面值数组中面值小于等于amount的那些元素
        for v in [x for x in values if x <= amount]:
            # 用面值为v的硬币+其他硬币找零所需的最少硬币数
            print(v, amount - v)
            min_num = 1 + minCoins(amount - v)
            # 判断min_num和ret_min的大小，更新ret_min
            if min_num < ret_min:
                ret_min = min_num
    # 更新缓存数组
    cache[amount] = ret_min
    recursion_num += 1
    return ret_min

def main():
    pass
    init(63)
    print('找零钱问题',minCoins(63))
    # print(cache)
    # print(recursion_num)
#
main()