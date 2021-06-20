#121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the current min 
        # then calculated the diff, if the diff is bigger then record the 
        # [1, 2]
        # [1, 7]
        if not prices: return 0
        minVal = float("inf")
        maxDiff = 0
        for p in prices:
            if p < minVal:
                minVal = p
            else:
                if p - minVal > maxDiff:
                    maxDiff = p - minVal
        return maxDiff  #O(n), O(1)
