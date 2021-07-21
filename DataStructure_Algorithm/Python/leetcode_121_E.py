# 121. Best Time to Buy and Sell Stock
from tying import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,5,3,6,4] -> don't have to be smallest value to max
        # [2,5,1,3,6,7] -> such as this does not apply
        # just need to find relative small and large value with higest profit
        if not prices:
            return 0
        profit, minVal = 0, float("inf")
        for val in prices:
            if val < minVal:  # valley
                minVal = val
            elif val - minVal > profit:
                profit = val - minVal
        return profit  # O(n), O(1)


# Solution2: thrid attempt by myself
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [1,1,1,1]
        #. ip
        p = profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[p]:
                p = i
            else:
                profit = max(profit, prices[i] - prices[p])
        return profit
