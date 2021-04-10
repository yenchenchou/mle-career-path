class Solution:
    def sort(self, nums):
        for i in range(len(nums)-1):
            minIndex = float("inf")
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    minIndex = j
            nums[minIndex], nums[i] = nums[minIndex], nums[i]