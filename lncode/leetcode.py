class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag = 0
        find_index = 0
        while flag < len(nums) - 1:
            find = 0
            for i in range(flag + 1, len(nums)):
                if nums[flag] + nums[i] == target:
                    find = 1
                    find_index = i
                    break
            if find:
                break
            flag = flag + 1

        if find_index:
            return [flag, find_index]

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n, res = len(nums), []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    r = r - 1
                    while l<r and nums[l] == nums[l-1]:
                        l = l +1
                    while l < r and nums[r] == nums[r+1]:
                        r = r -1
                elif tmp >0:
                    r = r -1
                else:
                    l = l +1

        return res

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        reverse_x = str(x)
        flag = 0
        if str(x)[0] == '-':
            flag = 1
            reverse_x = str(x)[1:]

        i = len(reverse_x)-1
        reverse_str = ''
        not_xiao_zone = 0
        while i>=0:
            if not_xiao_zone==0 and reverse_x[i]== '0':
                i = i - 1
                continue
            not_xiao_zone = 1
            reverse_str = reverse_str + reverse_x[i]
            i = i -1

        back_int = -int(reverse_str) if flag else int(reverse_str)

        if back_int>= -2**31 and back_int<=2**31-1:
            return back_int
        else:
            return 0

    def reverseBits(self, n):
        b = '{:032b}'.format(n)
        breverse = "".join(b[::-1])
        return int(breverse, 2)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1)+len(nums2))%2 ==1:
            zhongwei = [int(len(nums1)+len(nums2)/2), int(len(nums1)+len(nums2)/2)]
        else:
            zhongwei = [int(len(nums1)+len(nums2)/2), int(len(nums1)+len(nums2)/2)+1]
        index = 1
        i, j = 0, 0
        if nums1[0]<= nums2[0]:
            self.digui(nums1, nums2, i, j, index)
        else:
            self.digui(nums2, nums1, i, j, index)


    def digui(self, nums1, nums2, i, j, index):
        for v1 in range(i, len(nums1)):
            if nums1[v1] <= nums2[j]:
                index = index + 1
                i = v1
            else:
                for v2 in range(j, len(nums2)):
                    if nums2[v2] <= nums1[i + 1]:
                        index = index + 1
                        j = v2


# a = Solution()
# b = a.twoSum([2, 7, 11, 15], 17)
# print(b)
#
# nums = [-1, 0, 1, 2, -1, -4]
# b = a.threeSum(nums)
# print(b)
#
# print(a.reverseBits(121))

import re

reg = re.compile(',|\s')
s1 = '- 1212,00.135'
a = reg.sub('', s1)
print(int(float(a)*100))


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [1 for i in range(n)]

        i = 2
        while i * i < n:
        	if isPrime[i]:
        		j = i * i
        		while j < n :

        			isPrime[j] = 0
        			j += i
        	i += 1

        return sum(isPrime[2:])


a='1213'
print(a[::-1])

from collections import deque
d = deque()
d.extendleft(a)
print(d)
print(''.join(d))


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(S)):
            if S[i] == C:
                res.append(0)
                continue

            r = S.find(C, i + 1)
            l = S.rfind(C, 0, i) if i != 0 else -1
            if l != -1 and r != -1:
                res.append(min(i - l, r - i))
            else:
                res.append(i - l) if r == -1 else res.append(r - i)

        return res
