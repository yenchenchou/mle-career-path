# 3. Longest Substring Without Repeating Characters

# Solution1: brute fource
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # solution 
        # abcabcbb, pwwkew
        charSet = set()
        left, res = 0, 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(len(charSet), res)
        return res

# Solution2: sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcabcbb
        # ababcdf
        # aaa
        # pwwkew
        seen = dict()
        res = start = 0
        for i, val in enumerate(s):
            if val in seen:
                start = max(start, seen[val]+1)
            res = max(res, i - start + 1)
            seen[val] = i
        return res  # O(n), O(n)
