# 33. Search in Rotated Sorted Array
# Follow up: Can you achieve this in O(log n) time complexity?

# thoughts
# 1. split the scenario by mid
# 2. compare the position and see what kind of direction should the pointer go
#    for exmaple, there are three cases but two outcomes,
#    [target on left > mid], [target on right < mid], [target on right > mid]
# Solution1: binary search + two pass: find index with smallest value then get the target index
# Solution2: binary search + one pass
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            # elif nums[right] <= nums[mid] // nums[right] < nums[mid] are both okay -> need = at some where to stop the loop
            elif nums[mid] >= nums[left]:  # or nums[right], must have '=' to deal tew element
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
# We know that the point to know whether to go left / right
# before that, we need to the pointer is at the unrotated side or not.