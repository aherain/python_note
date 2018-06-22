
alist = [23,54,6,787,88,1,-1]

def bubbleSort(ls):
    exchanges = True
    for i in range(len(ls)-1,0,-1):
        if exchanges:
            exchanges = False
            for j in range(i):
                if ls[j] > ls[j+1]:
                    exchanges = True
                    temp = ls[j]
                    ls[j] = ls[j+1]
                    ls[j+1] = temp

# bubbleSort(alist)#冒泡排序与短冒泡排序
# print('冒泡排序与短冒泡排序的结果', alist)

def selectSort(ls):
    for lt in range(len(ls)-1,0,-1):
        positionOfMax = 0
        for it in range(1,lt+1):
            if ls[it]>ls[positionOfMax]:
                positionOfMax = it

        temp = ls[lt]
        ls[lt] = ls[positionOfMax]
        ls[positionOfMax] = temp

# selectSort(alist)
# print('选择排序的结果:', alist)

def insertSort(ls):
    for i in range(1,len(ls)):
        pos = i
        val = ls[i]
        while pos>0 and ls[pos-1]>val:
            ls[pos] = ls[pos-1]
            pos = pos-1
        ls[pos] = val

# insertSort(alist)
# print('插入排序的结果:', alist)

def shellSort(ls):
    n = len(ls)

    gap = n//2
    while gap > 0:
        #gap =1 就是普通的插入排序
        for i in range(gap, n):
            temp = ls[i]
            j= i
            while j>=gap and ls[j-gap] > temp:
                ls[j] = ls[j-gap]
                j = j-gap
            ls[j] = temp
        #普通的插入排序

        gap = gap //2

# shellSort(alist)
# print('希尔排序的结果', alist)

from collections import deque
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged,left,right = deque(),deque(left),deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)
        return merged

    middle = int(len(lst) // 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

# merge_sort(alist)
# print("归并排序的结果", merge_sort(alist))

#快速排序
def quicksort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quicksort(lst, lo, p)
        quicksort(lst, p+1, hi)
    return

def partition(lst, lo, hi):
    pivot = lst[hi-1]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[hi-1] < lst[i+1]:
        lst[i+1], lst[hi-1] = lst[hi-1], lst[i+1]
    return i+1
quicksort(alist, 0, len(alist))
print('快速排序的结果', alist)