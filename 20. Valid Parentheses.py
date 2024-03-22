class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(':')', '{':'}','[':']'}
        sTack = []
        for i in s:
            if i in '([{':
                sTack.append(i)
            elif len(sTack) == 0 or i != dic[sTack.pop()]:
                return False
        return len(sTack) == 0
'''''
r = Solution()
s = "()[]{}"
print(r.isValid(s))'''