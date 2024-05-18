class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        else:
            sign = 1
        res = 0
        for i in s:
            if not i.isdigit():
                break
            else:
                res = res*10+int(i)

        if sign == -1:
            return max(res*-1,-2**31)
        else:
            return min(res,2**31-1)
