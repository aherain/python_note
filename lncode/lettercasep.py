class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for s in S:
            print('打印每一次的res', res)
            if not s.isalpha():
                for i in range(len(res)):
                    res[i] += s
            else:
                for i in range(len(res)):
                    tmp = res[i]
                    res[i] += s.lower()
                    res.append(tmp + s.upper())

        return res


a = Solution()
S = '12a5B'
a.letterCasePermutation(S)


class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split(' ')))
        return sum(min(a,b) for a,b in zip(L, L[1:]) )
