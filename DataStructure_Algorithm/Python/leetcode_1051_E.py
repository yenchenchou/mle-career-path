# 1051. Height Checker
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        cnt = 0
        for real, exp in zip(heights, expected):
            if real != exp:
                cnt += 1
                
        return cnt
