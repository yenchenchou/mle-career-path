# 643. Maximum Average Subarray I

# Solution 1: time limit exceeded -> O(n^2)
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         maxAvg = sum(nums[:k])
#         avg = maxAvg
#         for i in range(1, len(nums)-k+1):
#             avg -= nums[i-1]
#             avg += nums[i+k-1]
#             if avg > maxAvg:
#                 maxAvg = avg
#         return maxAvg / k


# Solution2: Sliding window: The better way to do is calulate a default sliding window value and minus and add at the same time -> O(n)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = float("-inf")
        for i in range(len(nums) - k + 1):
            avg = sum(nums[i : i + k]) / k
            if avg > maxAvg:
                maxAvg = avg
        return maxAvg  # O(n), O(1)
