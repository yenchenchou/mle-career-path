# 1047. Remove All Adjacent Duplicates In String


class Solution:
    def removeDuplicates(self, S: str) -> str:
        # scan
        # stack[-1] == val
        stack = []
        for val in S:
            if stack and val == stack[-1]:
                stack.pop()
            else:
                stack.append(val)

        return "".join(stack)  # O(n), O(n)
