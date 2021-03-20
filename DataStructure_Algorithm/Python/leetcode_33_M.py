# 33. Search in Rotated Sorted Array
# thoughts 
    # 1. split the scenario by mid
    # 2. compare the position and see what kind of direction should the pointer go
    #    for exmaple, there are three cases but two outcomes, 
    #    [target on left > mid], [target on right < mid], [target on right > mid]
# Solution1: binary search + two pass: find index with smallest value then get the target index

# Solution2: binary search + one pass
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right-left)//2+ left
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                # elif target >= nums[left] and target > nums[mid]:
                #     left = mid + 1
                # elif target < nums[left]:
                #     left = mid + 1
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                # elif target <= nums[right] and target < nums[mid]:
                #     right = mid - 1
                # elif target > nums[right]:
                #     right = mid - 1
        return -1