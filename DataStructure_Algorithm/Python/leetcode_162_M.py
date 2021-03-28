
# 162. Find Peak Element
# Solution1 : linear search and compare the left and right neignbors. 
# Ituitive but have to handle cases where len == 2, or the head and tail position
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                return i
        if nums[0] < nums[-1]:
            return len(nums)-1
        else:
            return 0
        #[2], [1,2], [1,3,2], [1,2,3]
    # O(n), O(1)

# Solution 1.2: Linear search and compare the curr and the next index
# observation is that if it is not peak then the number will continue to go up, if it is peak
# then the next number is smaller or the peak is at the beginning
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1
    # O(n), O(1)

# Solution 2: Binary Search Iteration
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (right-left)//2 + left
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left #[1,2], [1,3,2]
    # O(logn), O(1)
        
# Solution3: Recursive Binary Search