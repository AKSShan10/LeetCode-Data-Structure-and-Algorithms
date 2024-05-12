# This solutions doesnot full-fill the size contrains. out of limit showed in the submission
# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         n1 = len(nums1)
#         n2 = len(nums2)
#         arr = []
#         i = j = 0
#         for c in range(0, n1+n2):
#             if i < n1 and j < n2:
#                 if nums1[i] > nums2[j]:
#                     arr.append(nums2[j])
#                     j += 1
#                 else:
#                     arr.append(nums1[i])
#                     print(arr)
#                     i += 1
#             elif i < n1:
#                 arr.append(nums1[i])
#                 i += 1
#             else:
#                 arr.append(nums2[j])
#                 j += 1
#         print(arr)
#         if len(arr) % 2 == 0:
#             d = len(arr) // 2
#             return float(((arr[d]+arr[d-1])/2.0))
#         else:
#             d = len(arr) // 2
#             return float(arr[d])
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        i = j = 0
        m1 = m2 = 0
        for c in range(0, (n1 + n2) // 2 + 1):
            m2 = m1
            if i < n1 and j < n2:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < n1:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1

        if (n1 + n2) % 2 == 0:
            return float((m1 + m2) / 2.0)
        else:
            return float(m1)


r = Solution()
n = [1,2]
n1 = [3,4]
m = r.findMedianSortedArrays(n,n1)
print(m)
