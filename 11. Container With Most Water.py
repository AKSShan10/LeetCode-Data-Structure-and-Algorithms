# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         maxstorage = 0
#         for i in range(n-1):
#             l = 0
#             r = l+1
#             for j in range(i+1,n):
#                 if height[i]<=height[j]:
#                     c = height[i]*(r-l)
#                 else:
#                     c = height[j]*(r-l)
#                 if c > maxstorage:
#                     maxstorage = c
#                 else:
#                     maxstorage = maxstorage
#                 r+=1
#             l +=1
#         return maxstorage
#     # Time limit exceeded
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
