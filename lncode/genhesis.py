class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        mp = [[""], ["()"]]
        for i in range(2, n + 1):
            mp.append([])
            for j in range(i):
                for x in mp[j]:
                    for y in mp[i - 1 - j]:
                        mp[i].append("(" + x + ")" + y)
        return mp[-1]

a = Solution()
print(a.generateParenthesis(3))