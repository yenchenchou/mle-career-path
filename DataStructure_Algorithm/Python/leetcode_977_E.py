#977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for val in nums:
            res.append(val*val)
        return sorted(res)
