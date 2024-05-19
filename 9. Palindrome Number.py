# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         a = []
#         while x > 0:
#             res = x % 10
#             a.append(res)
#             x = x//10
#         n = len(a)
#         c = False
#         for i in range(n//2+1):
#             if a[i] != a[n-1-i]:
#                 return False
#             else:
#                 c = True
#         return c
#     # list out of range
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        res = 0

        while temp > 0:
            d = temp % 10
            res = res * 10 + d
            temp = temp // 10
        return res == x
