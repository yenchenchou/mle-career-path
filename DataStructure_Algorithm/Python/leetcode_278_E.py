# 278. First Bad Version

# Solution1: brute force (not reccommended)
# Solution2: Iteration with Binary Search, this is not intuitive
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # We already know that 1 <= bad <= n <= 231 - 1
        # the API is called # def isBadVersion(version):

        left, right = 1, n
        while left <= right:
            mid = (right - left) // 2 + left
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1  # [g, b, b], [g, g, b]
        return left

    # O(logn), O(1)


# Solution2.2: Iteration with Binary Search, this better
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # We already know that 1 <= bad <= n <= 231 - 1
        # the API is called # def isBadVersion(version):

        left, right = 1, n
        while left < right:
            mid = (right - left) // 2 + left
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1  # [g, b, b], [g, g, b]
        return left


# Solution3: Recusion with Binary Search
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(1, n)

    def helper(self, left, right):
        if left == right:
            return left
        mid = (right - left) // 2 + left
        if isBadVersion(mid):
            return self.helper(
                left, mid
            )  # case [b, b] will show why mid -1 is produce error
        else:
            return self.helper(mid + 1, right)  # [b, b], [b, b, b]
