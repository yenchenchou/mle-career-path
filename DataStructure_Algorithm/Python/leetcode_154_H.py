# 154. Find Minimum in Rotated Sorted Array II

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
    
        # left, right = 0, len(nums)-1
        # while left < right:
        #     mid = (right-left)//2 + left
        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     elif nums[mid] < nums[right]:
        #         right = mid
        #     else:
        #         right = right - 1
        # return nums[left]