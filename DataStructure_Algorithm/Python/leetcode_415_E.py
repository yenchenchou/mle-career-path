# 415. Add Strings
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(self.helper(num1) + self.helper(num2))

    def helper(self, s):
        res = 0
        for val in s:
            res = res * 10 + int(val)
        return res  # O(n), O(1)
