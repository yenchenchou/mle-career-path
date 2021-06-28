# 219. Contains Duplicate II
# Solution 1: hash map adnd proess the map
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # create a map with index
        mapper = defaultdict(list)
        for i, val in enumerate(nums):
            mapper[val].append(i)
        for key, valList in mapper.items():
            if len(valList) > 1:
                # sliding window of size 2
                for i in range(len(valList) - 1):
                    if valList[i + 1] - valList[i] <= k:
                        return True
            else:
                continue
        return False  # O(nm), O(n)


# use set as sliding wondow
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()  # sliding window with len k
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s) > k:
                s.remove(nums[i - k])
        return False
