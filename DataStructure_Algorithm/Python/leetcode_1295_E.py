# 1295. Find Numbers with Even Number of Digits
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for val in nums:
            cnt = 0
            while val > 0:
                val //= 10
                cnt += 1
            if cnt % 2 == 0:
                res += 1
        return res
