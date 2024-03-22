class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[c] = nums[i]
            c += 1
        return c

'''''
check = Solution()

arr = [3,2,2,3]
print(check.removeElement(arr,3))'''