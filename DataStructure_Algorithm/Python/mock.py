"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6], k = 2
[7, 6, 5, 4, 3, 2, 1]
[5, 6, 7, 4, 3, 2, 1]
[5, 6, 7, 1, 2, 3, 4]

Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
    1 <= nums.length <= 105
    0 <= k <= 100000
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # for i in range(k):
        #     tmp = nums[-1]
        #     for j in range(0, len(nums)-1):
        #         nums[len(nums) - 1 -j] = nums[len(nums) - 2 - j]
        #     nums[0] = tmp
        k = k % len(nums)
        self.helper(nums, 0, len(nums)-1)
        self.helper(nums, 0, k-1)
        self.helper(nums, k, len(nums)-1)

    def helper(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1