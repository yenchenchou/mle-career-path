# 70. Climbing Stairs
# the central idea is still fibanocci

# Solution1: brute force top-down no memo, use mathematical induction n=1->1, n=2->2, n3->3, n=4->5, n=5->8
# Very easy to time-exceed
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    # O(2^n), O(n)


# Solution2: top-down with memo, use mathematical induction n=1->1, n=2->2, n3->3, n=4->5, n=5->8
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helper(n):
            if n<=2: return n
            if n not in cache.keys():
                cache[n] = helper(n-1) + helper(n-2)
            return cache[n]
        return helper(n)


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1:1, 2:2}
        def helper(n):
            if n not in cache.keys():
                cache[n] = helper(n-1) + helper(n-2)
            return cache[n]
        return helper(n)
    # O(n), O(n)


# Solution3: Iteratoin, Bottom-Up Approach using two var since fib only need the previous two numbers
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        prev1, prev2 = 2, 1
        for _ in range(3, n+1):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        return cur
    # O(n), O(1)