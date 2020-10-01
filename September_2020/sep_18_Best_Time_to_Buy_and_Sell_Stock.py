class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxPrice = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxPrice = max(maxPrice, price-minPrice)
        return maxPrice