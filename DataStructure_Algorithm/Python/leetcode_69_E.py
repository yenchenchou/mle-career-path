# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 0, x - 1
        # right = x//2
        while left <= right:
            mid = (right - left) // 2 + left
            num = mid * mid
            if num == x:
                return mid
            elif num > x:
                right = mid - 1
            else:
                left = mid + 1
        return right  # [1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]
#Follow up:
# Does x, x-1, x//2 matters? no, as long as x>=2 and x <= x//2 then is okay
# O(logn), O(1)
# Refer to  367 (perfect root)
