# Reverse a string and swap the string in place
# search for top and tail move toward the center and swap everytime 

# Solution 1: Iterative
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # give tow poiter, one from o, another from tail
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left -= 1
            right += 1 # [None], [1], [2,3]

# Solution2: Recursive
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # give tow poiter, one from o, another from tail
        def helper(left, right, s):
            s[left], s[right] = s[right], s[left]
            left -= 1
            right += 1 # [None], [1], [2,3]
            return helper(left, right, s)
            
        help(0, len(s)-1, s)