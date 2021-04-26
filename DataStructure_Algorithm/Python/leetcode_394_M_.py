# 394. Decode String

from collections import deque

# Solution1: use stack
class Solution:
    def decodeString(self, s: str) -> str:
        # when we hit open bracket, we need to handle the content in the brackets
        # we need stack to hold the numeric value for later calculation with the string
        stack = deque([])
        stack.append([[], 1])
        k = 0
        for val in s:  # O(n)
            if val.isdigit():
                k = (k * 10) + int(val)
            elif val == "[":
                stack.append([[], k])
                k = 0
            elif val == "]":
                newStringList, k = stack.pop()
                stack[-1][0].extend(newStringList * k)  # extend is O(Maxk)
                k = 0
            elif val.isalpha():
                stack[-1][0].append(val)
        return "".join(stack[0][0])  # O(n*k) -> string extend and loop, O(n)


# Solution1.2:
from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        # when we hit open bracket, we need to handle the content in the brackets
        # we need stack to hold the numeric value for later calculation with the string
        stack = deque([])
        stack.append(["", 1])
        k = 0
        for val in s:
            if val.isdigit():
                k = (k * 10) + int(val)
            elif val == "[":
                stack.append(["", k])
                k = 0
            elif val == "]":
                newStringList, k = stack.pop()
                stack[-1][0] += newStringList * k
                k = 0
            elif val.isalpha():
                stack[-1][0] += val
        return stack[0][0]


# Solution2: use recursion