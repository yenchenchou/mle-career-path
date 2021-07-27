# 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #[1,7,3,6,5,6] -> 28
        #[1,2,1]
        left, right = 0, sum(nums)
        for i, val in enumerate(nums):
            right -= val  # 11
            if left == right:
                return i
            left += val  # 11
        return -1