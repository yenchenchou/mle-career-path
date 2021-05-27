# 17. Letter Combinations of a Phone Number
# Solution1: DFS
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapper = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        stack = [""]
        res = []
        while stack:
            cur = stack.pop()
            if len(cur) == len(digits):
                res.append(cur)
            else:
                digitIndex = len(cur)
                characters = mapper[int(digits[digitIndex])]
                for char in characters:
                    stack.append(cur + char)
        return res  # O(n^2) from loop and the string concatenation, O(n)


# Solution2: BFS
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapper = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        queue = deque(mapper[int(digits[0])])
        for i in range(1, len(digits)):
            size = len(queue)
            while size:
                cur = queue.popleft()
                for j in mapper[int(digits[i])]:
                    queue.append(cur + j)
                size -= 1
        return queue  # O(jkn), O(n)
