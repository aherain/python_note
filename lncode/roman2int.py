class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        convert={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        for i in range(len(s)-1):
            #if (s[i]=='I' or s[i]=='X' or s[i]=='C') and convert[s[i]]<convert[s[i+1]]:
            if convert[s[i]]<convert[s[i+1]]:
                sum=sum-convert[s[i]]
            else:
                sum=sum+convert[s[i]]
        return sum+convert[s[-1]]

    def Int2roman(self, num):
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sb = []
        i=0
        while i < len(nums):
            count = int(num/nums[i])
            while count !=0:
                sb.append(romans[i])
                count = count - 1
            num = num%nums[i]
            i=i+1
        return ''.join(sb)

a=Solution()
print(a.Int2roman(9))
#找零钱的思路 将ＩＮＴ　转成　罗马数字


def ddd():
    strs = ['ew121', 'ew22', 'ew22']
    res = ''
    if len(strs) == 0:
        return ""

    for each in zip(*strs):
        print(each)
        if len(set(each)) == 1:
            res = res + each[0]
        else:
            return res
    return res

def dd():
    nums = [1,3,4]
    inst = ''.join(map(str,nums))
    print(inst)
    instd  = int(inst) + 1
    back_list = [int(i) for i in str(instd)]
    print(back_list)

def strStr():
    haystack = 'hello'
    needle = 'll'
    l = len(needle)
    for i in range(len(haystack)+1-l):
        if haystack[i:l+1] == needle:
            return i
    return -1

#重复子字符串的， 字符串长度大于1，应该为偶数，二分字符串相等
def repeated(s):
    kp = int(len(s) / 2)
    i = kp
    while i > 0:
        flg = True
        target = s[0:i]
        for j in range(i, len(s), len(target)):
            if target != s[j:j+len(target)]:
                flg = False
        if flg:
            return flg
        i = i - 1
    return False


def repeated_times(a, b):
    if len(a)>len(b):
        if b in a*2:
            return 1
        return -1
    if a == b:
        return 1
    for i in range(int(len(b)/len(a)),int(len(b)/len(a)+1)*2):
        print(b, a*i)
        if b in a*i:
            return i

    return -1


# "abc"
# "cabcabca"
A = "abc"
B = "cabcabca"

print('nihao',repeated_times(A, B))


class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if(A.count(B)>=1):
            return 1
        if(set(A)!=set(B)):
            return -1
        i=int(len(B)/len(A))
        while(1):
            C=A*i
            if(C.count(B)>0):
                return i
            if(i>2 and len(C)>2*len(B)):
                return -1
            i+=1

astr = ' dfd frefr, egfr ,,, rgrg'
print(astr.split())


#通过位运算找不重复的数字
#自己一自己的异或运算 是 0
#数字与0 的异或是 数字本身
print('asa',0^0, 1^2, 1^2^2^4^4)


def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1 if nums[0] == 0 else 0
    for i in range(len(nums)):
        tmp = nums[i]
        while tmp < len(nums) and nums[tmp] != tmp:
            nums[tmp], tmp = tmp, nums[tmp] #对应下标对应的数值

    print(nums)
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)

print(missingNumber([1,0,3]))


def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + ((r - l) >> 2)
        count = sum(num <= mid for num in nums)
        if count > mid:
            r = mid - 1
        else:
            l = mid + 1
    return l
print(findDuplicate([3,1,1]))

from hashlib import sha256


class Codec:
    def __init__(self):
        self._cache = {}
        self.url = 'http://tinyurl.com/'

    def encode(self, long_url):
        """Encodes a URL to a shortened URL.
        :type long_url: str
        :rtype: str
        """
        key = sha256(long_url.encode()).hexdigest()[:6]
        self._cache[key] = long_url
        return self.url + key

    def decode(self, short_url):
        """Decodes a shortened URL to its original URL.
        :type short_url: str
        :rtype: str
        """
        key = short_url.replace(self.url, '')
        return self._cache[key]

#找出有多少个1
def countDigitOne(self, n):
    k, m = 1, n
    while m > 0:
        k = int(k * 10)
        m = int(m / 10)
    return self.calculate(n, k)

def calculate(self, n, k):
    k = int(k)
    if n <= 0:
        return 0
    if n < 10:
        return 1
    while 1:
        c = int(n / k)
        if c != 0:
            break
        k = int(k / 10)

    if c == 1:
        return n - k + 1 + self.calculate(n - k, k / 10) + self.calculate(k - 1, k / 10)  # 如果能理解最高位将次高位分成若干份这句话
    else:
        return k + self.calculate(n - c * k, k / 10) + c * self.calculate(k - 1, k / 10)

def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    base, res = 5, 0
    while n >= base:
        res += n // base
        base *= 5
    return res

def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    cd1 = []
    cd2 = []
    for i in A:
        print(i % 2)
        if i % 2 == 0:
            cd1.append(i)
        else:
            cd2.append(i)

    cd1.sort()
    cd2.sort()

    return cd1+cd2

print(sortArrayByParity([3,1,2,4]))


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum, max_end = nums[0], nums[0]
    for i in range(1, len(nums)):
        max_end = max(max_end + nums[i], nums[i])
        max_sum = max(max_sum, max_end)
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


from collections import Counter
a = [0]
result = Counter(a)
print(result)

ms,ct = result.most_common(1)[0]
all_list = []
for i in result.most_common():
    if ct == i[1]:
        all_list.append(i[0])
    break

mind = len(a)-a[::-1].index(ms) - a.index(ms)
for c in all_list:
    mind = min(mind, len(a)-a[::-1].index(c) - a.index(c))

print(mind)


def isMonotonic(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    n = len(A)
    count1 = 0
    count2 = 0
    for i in range(0, n - 1):
        temp = A[i + 1] - A[i]
        if temp >= 0:
            count1 += 1
        if temp <= 0:
            count2 += 1
    if count1 == n - 1 or count2 == n - 1:
        return True
    else:
        return False

print(isMonotonic([6,5,3,4]))


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    ad = nums1 + nums2
    ad.sort()
    if len(ad) % 2 == 0:
        m = int(len(ad) / 2)
        mid = sum(ad[m - 1: m + 1]) / 2
    else:
        mid = ad[int(len(ad) / 2)]
    return mid


print(findMedianSortedArrays([1, 2], [3, 4]))
def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    lookup = {}
    for i in range(len(nums)):
        if nums[i] not in lookup:
            lookup[nums[i]] = i
        else:
            if i - lookup[nums[i]] <= k:
                return True
            else:
                lookup[nums[i]] = i
    return False

#每一次比较两个数组元素 大的元素放在排在尾部
def mn_sort(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m = m - 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n = n - 1
    if n > 0:
        nums1[:n] = nums2[:n]


nums1 = [12,23,45, None, None, None, None]
mn_sort(nums1,3, [11,24,77],3)
print('ddd',nums1)

pat = "abba"
str = "dog dog dog dog".split()
print(dict(zip(pat, str)))
print(len(set(zip(pat, str))))
print(len(set(pat)))
print(len(set(str)))


def reverseOnlyLetters(S):
    p = [i for i in S if i.isalpha()]
    print(p)
    b = ''.join([i if not i.isalpha() else p.pop() for i in S])
    print(b)

S = "Test1ng-Leet=code-Q!"
reverseOnlyLetters(S)

import collections

a = collections.Counter(["a","a","b","b","c","c","c"])
back_data = []
for c, v in a.items():
    print( c, v)
    back_data.append(c)
    if v != 1:
        back_data.append(v)
print(back_data)


#反转元音字母 【aeiou】
import re
s = 'hEllo'
vowels = re.findall('(?i)[aeiou]', s)
print(vowels)

def sf(m):
    return vowels.pop()
print(re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s))


rpt_type='xxxx'
f = "%s_report_list" % (rpt_type or "month")
print(f)

nums = [-1,0,3,5,9,12]
target = 9
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        print(left, right)
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [-1,0,3,5,9,12]
target = 2
print('二分查找结果', search(nums, target))


from collections import Counter
res = ["plpaboutit","jnoqzdute","sfvkdqf","mjc","nkpllqzjzp","foqqenbey","ssnanizsav","nkpllqzjzp","sfvkdqf","isnjmy","pnqsz","hhqpvvt","fvvdtpnzx","jkqonvenhx","cyxwlef","hhqpvvt","fvvdtpnzx","plpaboutit","sfvkdqf","mjc","fvvdtpnzx","bwumsj","foqqenbey","isnjmy","nkpllqzjzp","hhqpvvt","foqqenbey","fvvdtpnzx","bwumsj","hhqpvvt","fvvdtpnzx","jkqonvenhx","jnoqzdute","foqqenbey","jnoqzdute","foqqenbey","hhqpvvt","ssnanizsav","mjc","foqqenbey","bwumsj","ssnanizsav","fvvdtpnzx","nkpllqzjzp","jkqonvenhx","hhqpvvt","mjc","isnjmy","bwumsj","pnqsz","hhqpvvt","nkpllqzjzp","jnoqzdute","pnqsz","nkpllqzjzp","jnoqzdute","foqqenbey","nkpllqzjzp","hhqpvvt","fvvdtpnzx","plpaboutit","jnoqzdute","sfvkdqf","fvvdtpnzx","jkqonvenhx","jnoqzdute","nkpllqzjzp","jnoqzdute","fvvdtpnzx","jkqonvenhx","hhqpvvt","isnjmy","jkqonvenhx","ssnanizsav","jnoqzdute","jkqonvenhx","fvvdtpnzx","hhqpvvt","bwumsj","nkpllqzjzp","bwumsj","jkqonvenhx","jnoqzdute","pnqsz","foqqenbey","sfvkdqf","sfvkdqf"]
a = Counter(sorted(res))
print(a.most_common(1))


def isPerfectSquare(x):
    """
    :type num: int
    :rtype: bool
    """
    r = x
    while r * r > x:
        print('每次R值',(r + x / r) / 2)
        r = (r + x / r) / 2
        # r = r/2 + x/(2*r)
    return r * r == x

isPerfectSquare(9)