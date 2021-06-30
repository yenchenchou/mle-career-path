# 67. Add Binary


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a and b:
            return ""
        if not a:
            return b
        if not b:
            return a
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        res = []
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                res.append("1")
            else:
                res.append("0")
            carry //= 2
        if carry == 1:
            res.append("1")

        return "".join(reversed(res))  # O(n). O(n)
