# LaiOffer

# 1. Classic Binary Search
def binary_search(nums, target):
    if not nums: return nums
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target: 
            return nums[mid]
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    assert binary_search([2, 3, 4], 3) == 3
    assert binary_search([2, 4], 2) == 2
    assert binary_search([2, 4, 5, 7, 100], 7) == 7
    assert binary_search([2, 4, 5, 7, 100], 8) == -1


# 2. Binary Search on 2D array
def binary_search_2D(nums, target):
    # if not nums: print(nums)
    # if not nums[0]: print(nums)
    if not nums or not nums[0]: return -1
    left, right = 0, len(nums) * len(nums[0]) - 1
        
    while left <= right:
        mid = (left + right) // 2
        row = mid // len(nums[0])
        col = mid % len(nums[0])
        if nums[row][col] == target:
            return nums[row][col]
        elif nums[row][col] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    assert binary_search_2D([[2, 3, 4], [5, 6, 7]], 3) == 3
    assert binary_search_2D([[2, 3, 4], [5, 6, 7]], 9) == -1
    assert binary_search_2D([[4], [7]], 7) == 7
    assert binary_search_2D([[], []], 7) == -1

# 3. Search closest number
def binary_search_closest(nums, target):
    if not nums: return nums
    left, right = 0, len(nums)-1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target: 
            return nums[mid]
        elif nums[mid] > target:
            right = mid
        else:
            left = mid
    # post processing
    if abs(nums[left] - target)<= abs(nums[right] - target):
        return nums[left]
    else:
        return nums[right]


if __name__ == "__main__":
    assert binary_search_closest([2, 3, 4], 3) == 3
    assert binary_search_closest([2, 4], 1) == 2
    assert binary_search_closest([2, 4, 5, 7, 100], 66) == 100
    assert binary_search_closest([2, 4, 5, 7, 100], 8) == 7


# 4. 5. Search target number with the smallest index, given that the number can be duplicated
# [4, 5, 5, 5], target=5
def binary_search_smallest_index(nums, target): 
    if not nums: return nums
    left, right = 0, len(nums)-1
    while left + 1 < right:  # left < right is okay if not all right = mid, left - mid
        mid = (left + right) // 2
        if nums[mid] == target:
            right = mid  # left = mid for largest index
        elif nums[mid] < target:
            left = mid + 1  # both left = mid okay
        else:
            right = mid - 1  # both right = mid okay

    # swap the order if largest index target
    if nums[left] == target:
        return left         
    elif nums[right] == target:
        return right
    else:
        return -1

if __name__ == "__main__":
    assert binary_search_smallest_index([2, 3, 4], 3) == 1
    assert binary_search_smallest_index([2, 4, 4, 4], 4) == 1
    assert binary_search_smallest_index([2], 2) == 0
    assert binary_search_smallest_index([2, 4, 4], 4) == 1


# 658. Find K Closest Elements
# 6. Find k elememts that closet to the target number
# 中心開花
def binary_search_k_smallest(nums, target): 
    if not nums: return nums
    left, right = 0, len(nums)-1
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = self.binarySearch(arr, x)
        left, right = index, index
        while right - left < k:
            if left == 0: return arr[:k]
            if right == len(arr): return arr[-k:]
            if x - arr[left-1] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left: right]
        
    def binarySearch(self, arr, target):
        left, right = 0, len(arr)-1
        while left +1 < right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid
            else:
                right = mid
        if target - arr[left] <= arr[right] - target:
            mid = left
        else:
            mid = right
        return mid


# 7. (big variant) unkown size input, see if target is inside the input
# Sol: double search range to search right boundary
# Why niot 10 times each time.
# 702. Search in a Sorted Array of Unknown Size
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target: return 0
        left, right = 0, 1
        # double the search range, do it if the right most vlaue < target
        while reader.get(right) < target:
            left = right
            right *= 2
        
        while left <= right:
            mid = (left + right) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1