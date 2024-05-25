class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        res = self.b_search(s, e, nums, target)
        return res

    def b_search(self, start, end, nums, target):
        if start <= end:
            m = int(start + end) // 2
            if target == nums[m]:
                return m
            if target < nums[m]:
                return self.b_search(start, m - 1, nums, target)
            else:
                return self.b_search(m + 1, end, nums, target)

        return -1