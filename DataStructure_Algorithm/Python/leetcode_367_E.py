# 367. Valid Perfect Square

# Solution1: Binary Search
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return num
        left, right = 0, num-1
        while left <= right:
            mid = (right-left)//2+left
            val = mid * mid
            if val == num:
                return True
            elif val > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
    #O(logn) O(1)


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return num
        left, right = 1, num
        while left <= right:
            mid = (right-left)//2+left
            val = mid * mid
            if val == num:
                return True
            elif val > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
    #O(logn) O(1)

