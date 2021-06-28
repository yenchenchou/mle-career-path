# 53. Maximum Subarray


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # using variables to compare whether the curr or the accumulated sum is bigger
        max_subarray = cur_subarray = nums[0]
        for val in nums[1:]:
            cur_subarray = max(
                val, cur_subarray + val
            )  # this will cut the cummulation if see a larger number, mire like generating diff subarrays
            max_subarray = max(max_subarray, cur_subarray)
        return max_subarray
