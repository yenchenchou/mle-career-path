# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False
        seen = set()
        for val in nums:
            if val not in seen:
                seen.add(val)
            else:
                return True
        return False
