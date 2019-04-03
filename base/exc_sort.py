alist = [23,54,6,787,88,1,-1, 29]

#将冒泡排序变成短冒泡排序，提高效率
def bubbleSort(ls):
    exchanges = True
    for i in range(len(ls)-1,0,-1):
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


def selectSort(ls):
    for lt in range(len(ls)-1, 0, -1):
        positionOfMax = 0
        #找到列表中最大的值的下标，每次都需要将数组的待排序部分，从新扫描一遍
        for it in range(0, lt+1):
            if ls[it]>ls[positionOfMax]:
                positionOfMax = it
        #把他交换到未排序的最后位置
        temp = ls[lt]
        ls[lt] = ls[positionOfMax]
        ls[positionOfMax] = temp
# selectSort(alist) #两个循环遍历 每次找到最大的放在数组的最后面
# print('选择排序的结果:', alist)




#插入排序，顾名思义找到一个数的应有位置，然后插入进去
def insertSort(ls):
    for i in range(1, len(ls)):
        pos, val = i, ls[i]
        while pos > 0 and ls[pos-1] > val:
            ls[pos] = ls[pos-1]
            pos = pos - 1  # 预留第一个位置，然后向前追溯，找到适合的位置放置当前值。
        ls[pos] = val

# insertSort(alist)
# print('插入排序的结果:', alist)


#希尔排序就是分 gap 的插入排序, 分间隔的插入排序，每一次插入排序是数组渐变成有序数组
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
            dd = left.popleft() if left[0] <= right[0] else right.popleft()
            merged.append(dd)

        merged.extend(right if right else left)
        return merged
    middle = int(len(lst) // 2)

    left = merge_sort(lst[:middle])#左拆
    right = merge_sort(lst[middle:])#右拆 然后合并在一起
    return merge(left, right)
# merge_sort(alist)
from collections import deque
def merge_sort(ls):
    if len(ls)<=1:
        return ls
    def merge(left, right):
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            dd = left.popleft() if left[0]<=right[0] else right.popleft()
            merged.append(dd)

        merged.extend(right if right else left)
        return merged
    middle = int(len(ls)//2)
    left = merge_sort(ls[:middle])
    right = merge_sort(ls[middle:])
    return merge(left, right)


#Talk is cheap, show the code
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

nums = [6, 1,2,7,9,3,4,5,-1,8]
print('打印快速排序的结果：', quicksort(nums))
