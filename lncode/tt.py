str = "this is really a string example....wow!!!"
substr = "is"

print(str.rfind(substr))
print(str.rfind(substr, 0, 10))
print(str.rfind(substr, 10, 0))

print(str.find(substr))
print(str.find(substr, 0, 10))
print(str.find(substr, 10, 0))



class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def helper(log):
            _id, rest = log.split(" ", 1)
            return (0, rest, _id) if rest[0].isalpha() else (1,)

        return sorted(logs, key=helper)



http://192.168.1.211:12018/inner/outpush/settle_detail?pid=22222