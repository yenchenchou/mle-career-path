# 4. Median of Two Sorted Arrays in O(logn)

# Solution1 Video
# https://www.youtube.com/watch?v=LPFhl65R7ww&t=1249s
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find the rules
        # if we know the maxLeftX <= minRighty and maxRightX <= minRightX then we find median
        # so we random cut off points, but how to adjust the points
            # the partitionX + partitionY is equal or larger only size pof one
            # every element in left partition <= every element in right partition
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)
        left, right = 0, n
        while left <= right:
            partitionX = (left + right) // 2
            partitionY = (n + m + 1) // 2 - partitionX
            # now check the condition maxLeftX <= minRighty and maxRightX <= minRightX 
            maxLeftX = float("-inf") if partitionX == 0 else nums1[partitionX-1]
            minRightX = float("inf") if partitionX == n else nums1[partitionX]
            maxLeftY = float("-inf") if partitionY == 0 else nums2[partitionY-1]
            minRightY = float("inf") if partitionY == m else nums2[partitionY]
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (n + m) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1


# Solution2: 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
            
        nums1Min, nums1Max, half = 0, m, (m+n+1)//2
        while nums1Min <= nums1Max:
            mid1 = (nums1Max+nums1Min)//2
            mid2 = half - mid1
            if mid1>0 and nums1[mid1-1] > nums2[mid2]:
                nums1Max = mid1 - 1
            elif mid1 < nums1Max and nums2[mid2-1] > nums1[mid1]:
                nums1Min = mid1 + 1
            else:
                if mid1 == 0:
                    max_of_left = nums2[mid2-1]
                elif mid2 == 0:
                    max_of_left = nums1[mid1-1]
                else:
                    max_of_left = max(nums1[mid1-1], nums2[mid2-1])
                    
                if (m+n)%2 == 1:
                    return max_of_left
                
                if mid1 == m:
                    min_of_right = nums2[mid2]
                elif mid2 == n:
                    min_of_right = nums1[mid1]
                else:
                    min_of_right = min(nums2[mid2], nums1[mid1])
                    
                return (max_of_left + min_of_right)/2

# O(logn), O(1)