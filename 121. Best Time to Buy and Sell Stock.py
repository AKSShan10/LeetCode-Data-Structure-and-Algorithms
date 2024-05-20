class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        min_price = prices[0]
        for i in prices[1:]:
            p = max(p,i-min_price)
            min_price = min(min_price,i)
        return p