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
        