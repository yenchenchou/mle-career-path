# 7. Reverse Integer
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            flag = 1
        else:
            x = -x
            flag = -1

        res = 0
        while x > 0:
            val = x % 10
            x = x // 10
            res = 10 * res + val
        res = res * flag
        if -(2 ** 31) <= res <= 2 ** 31 - 1:
            return res
        else:
            return 0  # O(n), O(1)
