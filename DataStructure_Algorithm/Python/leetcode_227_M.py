# 227. Basic Calculator II

from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        # is there +1-3
        # handle operand:
        # 1, 10, -> cur = 0, cur = cur*10 + int(val), cur=0
        # since the operator is to calculate with the nex digit, er need a var to hold the operator
        # since calculate the next number, we need to hold prev value
        # since we will refresh the curand prev, we need res to store last action
        res, cur, prev = 0, 0, 0
        operator = "+"
        # stack = deque(1)
        for val in s + "+":
            if val.isdigit():
                cur = cur * 10 + int(val)
            elif val != " ":
                if operator == "+" or operator == "-":
                    res += prev
                    prev = cur if operator == "+" else -cur
                elif operator == "*" or operator == "/":
                    prev = (
                        cur * prev if operator == "*" else int(prev / cur)
                    )  # no prev//cur dur to negative num
                cur, operator = 0, val

        res += prev
        return res
