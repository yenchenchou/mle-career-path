# 374. Guess Number Higher or Lower


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == -1:
                right = mid - 1
            else:
                left = mid + 1  # O(logn), O(1)
