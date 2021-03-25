# 350. Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        res = []
        for val in nums1:
            if val not in dic:
                dic[val] = 1
            else:
                dic[val] += 1
        for val in nums2:
            if val in dic and dic[val] > 0:
                dic[val] -= 1
                res.append(val)
            else:
                continue
        return res
                
# O(n+m)->O(n), O(n): the space to store dic and result

# This is the problem that will merge with MapReduce, see discussion here :https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82243/Solution-to-3rd-follow-up-question