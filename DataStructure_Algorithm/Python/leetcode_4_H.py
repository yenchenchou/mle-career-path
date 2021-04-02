# 4. Median of Two Sorted Arrays in O(logn)
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