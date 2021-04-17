# 154. Find Minimum in Rotated Sorted Array II

# Solution1.1: Binary search and specify the ----\/--- but the condition should be the same
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[left] == nums[right] == nums[mid]:
                right -= 1
            elif nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

    # O(n), O(1)


# Solution1.2: Binary search but if nums[mid] == nums[right] then move only once
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1,3,5]
        # [5,1,5]
        # [5,1,1]
        # [3,6,2,2]
        # [1,1,1]
        # [1,2,2]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:  # on the right
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]


# Compare to #153, having duplicates make the time complexity to be O(n)