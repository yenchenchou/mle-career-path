# 15. 3Sum

# Solution1: two pointer and fix one value a time
# Then becareful of duplicat results when you have duplicates numbers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort and fix one value at a time
        # make the same two sume function
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, i, res):
        # [-2,1,1,1,1,1]
        l ,r = i+1, len(nums)-1
        while l < r:
            s = nums[l] + nums[r] + nums[i]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # the most difficult part is to notice cases like: [-2,1,1,1,1,1]
                # this prevent duplicates results
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif s > 0:
                r -= 1
            else:
                l += 1