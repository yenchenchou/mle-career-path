# 1209. Remove All Adjacent Duplicates in String II

# Solution1.1: Use stack to store char and count with init
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # brute force
        stack = [["#", 0]]
        for val in s:
            if stack[-1][0] == val:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([val, 1])
        return "".join(val * cnt for val, cnt in stack)


# Solution1.2: Use stack to store char and count without init
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # deeedbbcccbdaa
        stack = []
        for val in s:
            if len(stack) == 0 or stack[-1][0] != val:
                stack.append([val, 1])
            elif stack[-1][0] == val:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        return "".join(val * cnt for val, cnt in stack)
