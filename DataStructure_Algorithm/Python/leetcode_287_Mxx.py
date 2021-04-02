# 287. Find the Duplicate Number
# Solution1: use hash map to save the value

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for val in nums:
            if val not in dic:
                dic[val] = 1
            else:
                return val
# O(n), O(n)

# Solution2: Use Floyd's Tortoise and Hare (Cycle Detection)