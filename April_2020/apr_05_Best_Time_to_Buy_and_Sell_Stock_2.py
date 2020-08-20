class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)==0:
            return 0
        res = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                res += (prices[i+1]-prices[i])
        return res