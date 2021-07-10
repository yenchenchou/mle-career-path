#27. Remove Element

# Solution1
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# Solution2
class Solution:
        # [3,2,2,3], val = 3
        slow = fast = 0
        while fast < len(nums):
            if nums[slow] != val:
                slow += 1
            elif nums[slow] == val and nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        
        return slow