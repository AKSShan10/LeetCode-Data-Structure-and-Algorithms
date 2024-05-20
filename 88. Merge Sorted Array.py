# class Solution:
#     def merge(self, nums1, m: int, nums2, n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         if m == 0:
#             return nums2
#         c = m + n - 1
#         m1 = m - 1
#         n1 = n - 1
#
#         while c > 0:
#             if nums2[n1] >= nums1[m1] and n1>=0 and m1>=0:
#                 nums1[c] = nums2[n1]
#                 n1 -= 1
#             elif nums2[n1] < nums1[m1]:
#                 nums1[c] = nums1[m1]
#                 m1 -= 1
#             elif n1<0 and m1 > 0:
#                 return nums1
#             else:
#                 nums1[c] = nums2[n1]
#                 n1 -= 1
#             c -= 1
#
#         return nums1
# m = Solution()
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# r = m.merge(nums1, 3, nums2,3)
# print(r)
# this one does not follow the third conditions
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 :
            return
        l_a = m+n
        c = l_a-1
        while n > 0 and m > 0 :
            if nums2[n-1] >= nums1[m-1]:
                nums1[c] = nums2[n-1]
                n-=1
            else:
                nums1[c] = nums1[m-1]
                m-=1
            c-=1
        while n > 0:
            nums1[c] = nums2[n-1]
            n-=1
            c-=1