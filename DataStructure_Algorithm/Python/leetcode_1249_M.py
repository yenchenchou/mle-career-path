# 1249. Minimum Remove to Make Valid Parentheses
# Solution1:
# we record the index where ( exists
# if face ) but no elemets in stack, then we record the index
# the second iteration, we remove ( from the indexes
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # ()(
        # (
        # )
        stack_right = []
        stack_left = []
        for i in range(len(s)):
            if s[i] == "(":
                stack_left.append(i)
            elif s[i] == ")" and stack_left:
                stack_left.pop()
                continue
            elif s[i] == ")" and not stack_left:
                stack_right.append(i)
            else:
                continue
        res = []
        stack = stack_left + stack_right
        for i in range(len(s)):
            if i not in stack:
                res.append(s[i])
        return "".join(res)  # O(n^2), O(n)


# Solution 1.2: the logic is same as 1.1, but we use set for O(1) lookup the matched parentheses instead O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack_right = set()
        stack_left = []
        for i in range(len(s)):
            if s[i] == "(":
                stack_left.append(i)
            elif s[i] == ")" and stack_left:
                stack_left.pop()
                continue
            elif s[i] == ")" and not stack_left:
                stack_right.add(i)
            else:
                continue
        res = []
        stack_right = stack_right.union(set(stack_left))
        for i in range(len(s)):
            if i not in stack_right:
                res.append(s[i])
        return "".join(res)  # O(n), O(n)
