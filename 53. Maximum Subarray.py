class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxS = nums[0]
        curSum = 0
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxS = max(curSum,maxS)
        return maxS