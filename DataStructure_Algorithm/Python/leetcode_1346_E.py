# 1346. Check If N and Its Double Exist
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # only check on values can be divide by 2
        # set to store value, if a valid value arrive,
        # check whether the there is a value in the dic that that matches val//2
        # [7, 14]
        # [14, 7]
        seen = set()
        for val in arr:
            if (val % 2 == 0 and val // 2 in seen) or (val * 2 in seen):
                return True
            seen.add(val)
        return False  # O(n), O(1)
