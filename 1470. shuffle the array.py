class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        c = 0
        c1 = n
        check = []
        for i in range(0, n):
            check.append(nums[c])
            check.append(nums[c1])
            c1 = c1 + 1
            c = c + 1

        return check

'''''
result = Solution()
arr = [2,5,1,3,4,7]
print(result.shuffle(arr,3))
'''