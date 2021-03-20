# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        left, right = 0, x-1
        while left <= right:
            mid = (right-left)//2 + left
            num = mid * mid
            if num == x:
                return mid
            elif num > x:
                right = mid - 1
            else:
                left = mid + 1
        return right # [1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]

# Refer to  367 (perfect root)