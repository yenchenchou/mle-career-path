# 224. Basic Calculator
# 1+1, (1+2), (7-(8+9)), (1-(+1+1))
# Solution1: by observation, we know that
# operand can be form in multiple characters
# whenever we encounter operator, we calculate the res in the left side first and tag the operator sign for next operand calculation
# when we encounter (, we push the result so far to the stack and the sign and start fresh. The sign is to summary the operator you need for the next calculation
# if we face ")", we pop out the operand and signand refresh the operand. Before this, remember to update the result first hand
# In case there are oprand at last calculation, we do another res + sign * operand calculation at the last round
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        operand = 0  # cache the current operand
        res = 0  # the result between "(" and ")"
        sign = 1  # +-
        # (70-(+8-9))
        for val in s:
            if val.isdigit():
                operand = (operand * 10) + int(val)  # 70
            elif val == "+":
                res += sign * operand  # curret operand and the previous operator
                operand = 0
                sign = 1
            elif val == "-":
                res += sign * operand
                sign = -1
                operand = 0
            elif val == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif val == ")":
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        return res + sign * operand  # O(n), O(n)


# Solution2: store previous operand and the previous operator
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        cur = 0
        for val in "(" + s + ")":
            if val.isdigit():
                current = (10 * current) + int(val)
            elif val == "(":
                stack.extend([0, "+"])
                current = 0
            elif val != " ":
                operator, previous = stack.pop(), stack.pop()
                current = previous + (current if operator == "+" else -current)
                if val == ")":
                    continue
                stack.extend([current, val])
                current = 0
        return current  # O(n), O(n)
