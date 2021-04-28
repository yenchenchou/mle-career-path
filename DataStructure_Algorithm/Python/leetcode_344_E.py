# Reverse String
# Solution 1:  recusion swap
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left, right):
            if left < right:
                s[right], s[left] = s[left], s[right]
                right -= 1
                left += 1
                helper(left, right)
        helper(0, len(s)-1)  # [None], [1], [1, 2]
    # O(n), O(n)

# Solution 2:  iteration swap
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[right], s[left] = s[left], s[right]
            right -= 1
            left += 1
    # O(n), O(1)

# Solution 3: Recursion
class Solution:
    def reverseString(self, s: List[str]) -> None:
        return self.helper(s, 0, len(s)-1)

    def helper(self, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            return self.helper(s, left+1, right-1)


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left, right):
            if left < right:
                s[right], s[left] = s[left], s[right]
                helper(left+1, right-1)
        helper(0, len(s)-1)  # [1, 2]