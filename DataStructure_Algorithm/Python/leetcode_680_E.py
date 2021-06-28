# 680. Valid Palindrome II
# solution1: reversed string (faster, if [::-1] is allowed)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # aaaa baac, aac
        # two pointers
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one = s[left:right]
                two = s[left + 1 : right + 1]
                return one == one[::-1] or two == two[::-1]
            left += 1
            right -= 1
        return True  # O(n), O(n)


# Solution2: recursion
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(left, right, deleted):
            # abc
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    else:
                        return helper(left + 1, right, True) or helper(
                            left, right - 1, True
                        )
                else:
                    left += 1
                    right -= 1
            return True

        return helper(0, len(s) - 1, False)  # O(n), O(n)
