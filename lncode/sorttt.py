alist = [23,1,6,787,88,1,-1, 29]
def bubbleSort(sl):
    for i in range(len(sl)-1, 0 , -1):
        for j in range(i):
            if sl[j]>sl[j+1]:
                tmp = sl[j]
                sl[j] = sl[j+1]
                sl[j+1] = tmp
# bubbleSort(alist)
# print('冒泡排序', alist)

#选择排序每次选择最大的放在最后面
def selectSort(ls):
    for i in range(len(ls)-1, 0, -1):
        maxPoint = 0
        for j in range(i+1):
            if ls[j]> ls[maxPoint]:
                maxPoint = j
        tmp = ls[i]
        ls[i] = ls[maxPoint]
        ls[maxPoint] = tmp

# selectSort(alist)
# print('选择排次，每次选择较大的顺位排在后面', alist)

#插入排序，首部微有序的数据，次次插入有效值
def insertSort(ls):
    for i in range(1, len(ls)):
        pos, val = i, ls[i]
        while pos>0 and ls[pos-1]>val:
            ls[pos] = ls[pos-1]
            pos = pos - 1
        ls[pos] = val

def shellSort(ls):
    n, gap = len(ls), len(ls)//2
    while gap > 0:
        # for i in range(gap, n):
        #     tmp, j = ls[i], i
        #     while j >= gap and ls[j-gap] > tmp:
        #         ls[j], j = ls[j-gap], j - gap
        #     ls[j] = tmp
        gap = gap // 2
    #希尔排序不好写， 归并排序更难了
# shellSort(alist)

# print("希尔排序", alist)
from collections import deque
def merge_sort(lst):
    if len(lst)<=1:
        return lst
    def merge(left, right):
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            merged.append(left.popleft() if left[0]<= right[0] else right.popleft())
        merged.extend(right if right else left)
        return merged

    middle = int(len(lst)//2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)


#快速排序
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    less, greater = [], []
    base = nums.pop()
    for x in nums:
        print(base, x)
        if x < base:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less) + [base] + quicksort(greater)
# quicksort(alist)
# print("快速排序", quicksort(alist))


