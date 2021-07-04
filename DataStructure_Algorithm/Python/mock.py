"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]


nums = [2,2,2,2,2,2] target =2
[0, 5]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109, nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List, int


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if not nums:
            return result

        start = 0
        end = len(nums) - 1
    
         
        while start < end - 1:
            mid = (start - end) // 2
            # if nums[mid] == target:
            #     break
            elif nums[mid] >= target:
                end = mid
            elif nums[mid] < target:
                start = mid + 1
        else:
            return result


        left, right = mid, mid
        while nums[left] == target:
            left -= 1
        while nums[right] == target:
            right += 1

        return [left, right]


      
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first = self.searchFirst(nums, 0 , len(nums)-1, target)
        last = self.searchLast(nums, 0 , len(nums)-1, target)
        return [first, last]
        
    def searchFirst(self, nums, left, right, target):
        while left < right - 1:
            mid = (right-left)//2 + left
            # [1], [1,2], [1,2,2,2,3]
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
            
    def searchLast(self, nums, left, right, target):
        while left < right - 1:
            mid = (right-left)//2 + left
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1