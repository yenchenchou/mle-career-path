# 202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_num(n)
        return n == 1

    def get_num(self, n):
        res = 0
        while n > 0:
            num = n % 10
            n //= 10
            res += num ** 2
        return res
