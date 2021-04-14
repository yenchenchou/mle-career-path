# 20. Valid Parentheses
# Solution: Stack
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        # use dict to store valid pair and key-value pair
        # use stack to store the value if its pair is unseen
        stringMap = {"}": "{", ")": "(", "]": "["}
        stack = deque()
        for val in s:
            if val in stringMap.values():
                stack.append(val)
            elif val in stringMap.keys():
                if not stack or stack.pop() != stringMap[val]:
                    return False
            else:
                return False
        return not stack  # O(n), O(n)
