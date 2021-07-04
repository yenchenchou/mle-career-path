# 53. Maximum Subarray


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [-2, 1, -3]
        # [1, 1, -1]
        # compare inlclude the next ele or start new
        if not nums:
            return 0
        curr_array = final_array = float("-inf")
        for val in nums:
            curr_array = max(val, curr_array + val)  # handle where to start
            final_array = max(
                curr_array, final_array
            )  # handle where to end, record the previous subarray result
        return final_array
