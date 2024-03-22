class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = 0
        for i in range(len(nums),len(nums)*2):
            nums.append(nums[c])
            c+=1

        return nums
'''''
result = Solution()
arry  = [1,2,1]
print(result.getConcatenation(arry))'''
