# 26. Remove Duplicates from Sorted Array
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,1,2]
        if not nums:
            return 0
        p1 = p2 = 0
        while p2 < len(nums):
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
            p2 += 1
        return p1 + 1
