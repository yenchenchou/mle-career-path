# 122. Best Time to Buy and Sell Stock II

# Solution1: Dynamic programming
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = maxProfit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            low = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            high = prices[i]
            maxProfit += high - low
        return maxProfit
