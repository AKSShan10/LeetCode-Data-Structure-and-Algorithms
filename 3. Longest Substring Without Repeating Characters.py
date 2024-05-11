# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         n = len(s)
#         arr = []
#         for i in range(len(s)-1):
#             c = 1
#             for j in range(i+1,n):
#                 if s[i] != s[j]:
#                     c += 1
#                 else:
#                     arr.append(c)
#
#         print(arr)
#         return max(arr)
#
# r = Solution()
# k= r.lengthOfLongestSubstring("abcabcbb")
# print(k)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            res = max(res, (r - l) + 1)
            charSet.add(s[r])
        return res

