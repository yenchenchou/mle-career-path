# 316. Remove Duplicate Letters


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        stack = []
        dic = {val: key for key, val in enumerate(s)}
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i] < stack[-1] and i < dic[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(s[i])
                stack.append(s[i])
        return "".join(stack)  # O(n), O(n)
