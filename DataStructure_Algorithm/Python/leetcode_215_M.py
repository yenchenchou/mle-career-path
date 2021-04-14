# 215. Kth Largest Element in an Array


# Solution1: sort -> get [:k]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = self.mergeSort(nums)
        return nums[k - 1]

    def mergeSort(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(nums, left, right)

    def merge(self, nums, left, right):
        lp, rp, ap = 0, 0, 0
        while lp < len(left) and rp < len(right):
            if left[lp] > right[rp]:
                nums[ap] = left[lp]
                lp += 1
            else:
                nums[ap] = right[rp]
                rp += 1
            ap += 1
        if lp < len(left):
            nums[ap:] = left[lp:]
        if rp < len(right):
            nums[ap:] = right[rp:]
        return nums


# Solution2: heapify and keep <= k elements, if the new val is bigger then pop the smallest

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # is the array duplicated, so nlargest may be > n
        # does it has corner case?
        # how to meet the requirement:

        if not nums:
            return 0
        heap = []
        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, nums[i])
            else:
                heapq.heappushpop(heap, nums[i])
        return heap[0]  # [1, 4, 4]:k=2


# Solution2.2 : heapify and keep <= k elements, if the new val is bigger then pop the smallest
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        return heapq.nlargest(k, nums)[-1]