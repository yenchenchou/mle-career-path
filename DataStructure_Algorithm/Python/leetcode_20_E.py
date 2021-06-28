# 20. Valid Parentheses
# Solution: Stack
from collections import deque

# Solution1: need too much trick
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


# Solution2: General approach
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        mapper = {"[": "]", "(": ")", "{": "}"}
        stack = []
        for val in s:
            if val in mapper.keys():
                stack.append(mapper[val])
            elif not stack or stack[-1] != val:
                return False
            else:
                stack.pop()
        return not stack

# Solution3: my try
class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {"[": "]", "(": ")", "{": "}"}
        stack = []
        for val in s:
            if val in mapper:
                stack.append(val)
            else:
                if not stack or mapper[stack[-1]] != val:
                    return False
                else:
                    stack.pop()
        return not stack
