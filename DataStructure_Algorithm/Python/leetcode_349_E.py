# 349. Intersection of Two Arrays
# The solution is not hard but All the answers are using set() or .sort(), which may not be a valid way
# We should use Solution2 if the follow up questions pop out

# Solution1: use set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1) 
        set2 = set(nums2)
        return set1.intersection(set2)


# Solution2: Use merge sort and then use hashmap or using pointers
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pass
