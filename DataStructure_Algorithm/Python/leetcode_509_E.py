# 509. Fibonacci Number

# Solution1: Recursion, Top-Down Approach using Memoization
class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def helper(n):
            if n < 2: return n
            if n in cache.keys():
                return cache[n]
            cache[n] = helper(n-1) + helper(n-2)
            return cache[n]
        return helper(n) # 0 -> 0, 1 -> 1, 2 -> 1, 3 -> 2, 4 -> 2
    # O(n): porpagate to n to cache, O(n) store nth in hash table


# Solution2: Iteratoin, Bottom-Up Approach using Memoizationn
class Solution:
    def fib(self, n: int) -> int:
        cache = {0:0, 1:1}
        for i in range(2, n+1):
            cache[n] = cache[n-1] + cache[n-2]
        return cache[n]
    # O(n): porpagate to n to cache, O(n) store nth in hash table


# Solution3: Iteratoin, Bottom-Up Approach using two var since fib only need the previous two numbers
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        prev1, prev2 = 1, 0
        for _ in range(2, n+1)
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
    # O(n): porpagate to n to cache, O(n) store nth in hash table