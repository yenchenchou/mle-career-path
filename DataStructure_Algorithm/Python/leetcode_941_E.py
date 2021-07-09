# 941. Valid Mountain Array
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        ascFlag, dscFlag = False, False
        cache = arr[0]
        for val in arr[1:]:
            if val == cache:
                return False
            # The array must be increasing before any decreases
            elif val > cache and not dscFlag:
                ascFlag = True
            # If not, return False
            elif val > cache and dscFlag:
                return False
            # Under the condition that the array had increased before, it never goes up again once the array decreases.
            elif val < cache and ascFlag:
                dscFlag = True
            # If not, return False.
            elif val < cache and not ascFlag:
                return False
            cache = val
        return ascFlag and dscFlag
