# 485. Max Consecutive Ones


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxCount = 0
        for val in nums:
            if val == 1:
                cnt += 1
            else:
                cnt = 0
            maxCount = max(maxCount, cnt)
        return maxCount
