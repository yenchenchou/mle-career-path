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