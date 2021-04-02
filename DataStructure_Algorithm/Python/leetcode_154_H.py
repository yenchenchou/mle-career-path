# 154. Find Minimum in Rotated Sorted Array II

# Solution1: binary search and one step movement when nums[mid] == target
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (right-left)//2 + left
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right = right - 1
        return nums[left]
    # O(n), O(1)


# Solution 1.2: binary search and one step movement when nums[mid] == nums[left] == nums[right]
# we include nums[mid] <= nums[right] because nums[mid] == nums[right] has two condition
# when array is entirely sorted or a ---\/---- array. To enhance a bit, we can reduce the 
# chance of using O(n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (right-left)//2 + left
            if nums[left] == nums[right] == nums[mid]:
                right -= 1
            elif nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
    # O(n), O(1)

