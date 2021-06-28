# 14. Longest Common Prefix
# Solution1: scan vertoically
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        res = []
        for col in range(len(strs[0])):
            cnt = 0
            for row in range(len(strs)):
                if col < len(strs[row]) and strs[row][col] == strs[0][col]:
                    cnt += 1

            if cnt == len(strs):
                res.append(strs[0][col])
            else:
                break

        return "".join(res)  # O(mn), O(n)

# Solution1: use zip, take O(1) for zip, zip will omit the pairs that exceed the shortest iterable.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for row in zip(*strs):
            if len(set(row)) == 1:  # O(n)
                res.append(row[0])
            else:
                break

        return "".join(res)