class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        p_one, p_two  = 1, 1
        for i in range(n-1):
            temp = p_one
            p_one = p_one + p_two
            p_two = temp
        return p_one