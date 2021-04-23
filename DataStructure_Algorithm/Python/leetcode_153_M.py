# 153. Find Minimum in Rotated Sorted Array
# Solution 1.1: binary search


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        return nums[left] if nums[left] < nums[right] else nums[right]


# [1], [1,2], [1,2,3], [3,1,2], [4,5,6,7,0,1,2]
# O(n), O(1)


# Solution 1.2: binary search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    # [1], [1,2], [1,2,3], [2,1], [3,1,2], [4,5,6,7,0,1,2]


# When while left <= right,  left = mid + 1, right = mid - 1
# one of the pointer will out of index, so no post processing
# all element is examine, usually the output is related to mid point

# When while left < right,  left = mid + 1, right = mid
# on pointer will out of index bound, so post processing is allowed
# one element will remain un examined -> because of the left < right
# the output will related to left or right index

# when left <= right -> you need mid+1 and mid-1 -> 0 element left
# if you have erase one +1/-1 then left < right -> 1 element left
# both +1 amd -1 are erased then left < right - 1 -> 2 elements left