class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = []
        for i in range(0, len(nums) - 1):
            t = target - nums[i]
            j = i + 1
            if nums[j] == t:
                arr.append(i)
                arr.append(j)
                return arr
        return arr
