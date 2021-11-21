# 15. 3Sum

# Solution 1: two pointers, the key is to remove duplicates
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(i, nums, res)
        return res

    def twoSum(self, i, nums, res):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            tmp = nums[i] + nums[l] + nums[r]
            if tmp < 0:
                l += 1
            elif tmp > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                #
                while l < r and nums[l] == nums[l-1]:
                    l += 1  # O(n^2), O(n)
