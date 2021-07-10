# 905. Sort Array By Parity

# Solution1: two pointers from start


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow = fast = 0
        while fast < len(nums):
            if nums[slow] % 2 == 0:
                slow += 1
            elif nums[slow] % 2 != 0 and nums[fast] % 2 == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums  # O(n), O(1)


# Solution2: two pointers one fomr start one from end
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        return nums  # O(n), O(1)


# Compare 1 and 2:
# 1: slower but remain relative order, compactable with other questions
# 2: faster but don't remain relative order and too rough
