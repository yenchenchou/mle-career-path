# 658. Find K Closest Elements
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)-k
        while left < right:
            mid = (right-left)//2 + left
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            elif x - arr[mid] < arr[mid+k] - x:
                right = mid
            else:
                right = mid
        return arr[left: left+k]
#O(log(n-k))->O(logn), O(k)->O(n)


# 6. Find k elememts that closet to the target number
# 中心開花
# def binary_search_k_smallest(nums, target): 
#     if not nums: return nums
#     left, right = 0, len(nums)-1
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         index = self.binarySearch(arr, x)
#         left, right = index, index
#         while right - left < k:
#             if left == 0: return arr[:k]
#             if right == len(arr): return arr[-k:]
#             if x - arr[left-1] <= arr[right] - x:
#                 left -= 1
#             else:
#                 right += 1
#         return arr[left: right]
        
#     def binarySearch(self, arr, target):
#         left, right = 0, len(arr)-1
#         while left +1 < right:
#             mid = (left + right) // 2
#             if arr[mid] == target:
#                 return mid
#             elif arr[mid] < target:
#                 left = mid
#             else:
#                 right = mid
#         if target - arr[left] <= arr[right] - target:
#             mid = left
#         else:
#             mid = right
#         return mid
