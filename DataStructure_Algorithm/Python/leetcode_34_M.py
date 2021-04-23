# 34. Find First and Last Position of Element in Sorted Array

# Solution1.1: do two search, one for head one for tail


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first = self.searchFirst(nums, 0, len(nums) - 1, target)
        last = self.searchLast(nums, 0, len(nums) - 1, target)
        return [first, last]

    def searchFirst(self, nums, left, right, target):
        while left < right - 1:
            mid = (right - left) // 2 + left
            # [1], [1,2], [1,2,2,2,3]
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

    def searchLast(self, nums, left, right, target):
        while left < right - 1:
            mid = (right - left) // 2 + left
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1


# Solution1.2: do two search, one for head one for tail
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.searchLeft(nums, 0, len(nums) - 1, target)
        right = self.searchRight(nums, 0, len(nums) - 1, target)
        return (
            [left, right] if left <= right else [-1, -1]
        )  # when no matched value then right < left

    def searchLeft(self, nums, left, right, target):
        # [1,1,1,1], [1,1,2,2], [1,1]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchRight(self, nums, left, right, target):
        # [1,1]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right