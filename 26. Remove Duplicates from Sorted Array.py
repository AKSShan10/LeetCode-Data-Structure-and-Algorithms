class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        c = 0
        for i in range(len(nums)):
            # If the current element is equal to the next element, we skip
            if i < len(nums) - 2 and nums[i] == nums[i + 1]:
                continue
            # We will update the array in place
            nums[c] = nums[i]
            c += 1
        return nums

'''
check = Solution()

arr = [1,1,2]
print(check.removeDuplicates(arr))'''