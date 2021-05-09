# 34. Find First and Last Position of Element in Sorted Array

# Solution 1: Iteration + binary search and liner search when nums[mid] == target
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                start, end = mid, mid
                while start - 1 >= 0 and nums[start - 1] == target:
                    start -= 1
                while end + 1 < len(nums) and nums[end + 1] == target:
                    end += 1
                return [start, end]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]
#  O(n), O(1)


# Solution 2: 2 binary search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first = self.searchFirst(nums, 0, len(nums) - 1, target)
        last = self.searchLast(nums, 0, len(nums) - 1, target)
        return [first, last]

    def searchFirst(self, nums, left, right, target):
        while left < right:
            mid = (right - left) // 2 + left
            # [1], [1,2], [1,2,2,2,3]
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1

    def searchLast(self, nums, left, right, target):
        while left < right:
            # [1,2,2,2,3], [1,2]:t=1, [1,2]:t=2
            mid = (right - left) // 2 + left + 1
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        return left if nums[left] == target else -1


# other way of search first occurence
def find_first_occurence(nums, target):
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (right - left) // 2 + left
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] == target:
        return left
    else:
        return -1


# other way of search first occurence
def find_first_occurence(nums, target):
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums) - 1
    while left < right - 1:
        mid = (right - left) // 2 + left
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1


# other way of search last occurence
def find_last_occurence(nums, target):
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (right - left) // 2 + left + 1
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return left if nums[left] == target else -1


# other way of search last occurence
def find_last_occurence(nums, target):
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums) - 1
    while left < right - 1:
        mid = (right - left) // 2 + left
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1