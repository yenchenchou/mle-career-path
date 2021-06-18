# Input: nums = [1,12,3,0,0]
                            i
                        j
# Output: [1,3,12,0,0]
[1, 3, 12, 0, 0]

# Input: nums = [0]
# Output: [0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if num[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Input: prices = [7,6,4,3,1]
# Output: 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        for i in range(len(prices)-1):
            for j in range(1, len(prices)):
                diff = prices[j] - prices[i]
                if max_diff < diff:
                    max_diff = diff
        return max_diff

    

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
[-2, 1, -2, 4,  ]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Input: nums = [5,4,-1,7,8]
                [5,(9, 4), (8, -1), (15, 7), (23, 8)],
# Output: 23

class Solution:
    def maxSubArray(self, nums: List[int]) -> int: