class Solution:
    def groupAnagrams(self, strs):
        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)#改为元组存储
        return list(ans.values())


# a = Solution()
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(list(a.groupAnagrams(strs)))

# 1505969616

for k in zip([(1212,22),2,3], [4,5,6]):
    print(k)

#
# 专资：13516009329
# 院线：9607435717
# 差额: 3908573612
# 中影分账比：4200
