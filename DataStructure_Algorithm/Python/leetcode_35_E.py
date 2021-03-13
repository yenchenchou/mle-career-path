# 35. Search Insert Position
# Solution1: iteration, almost same question as #278
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # still a binary search problem
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right-left)//2+left
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left  #[1->1], [1->2], [1->0], [1,2]2, [1,2]1, [1,2,5],3