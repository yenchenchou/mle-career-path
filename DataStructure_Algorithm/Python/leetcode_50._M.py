# 50. Pow(x, n) -> Need to Review again

# Solution1: Iteration (brute force)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        num = 1
        for i in range(n):
            num = num * x
        return num
    #O(n), O(1)


# Solution1.2: Iteration (brute force)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: 
            x = 1/x
            n = -n
        res = 1
        while n:
            if n % 2 == 1:
                res = res * x
            x *= x
            n //= 2
        return res
    #O(logn), O(1)


# Solution2: Recursion: with using helper function
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: 
            x = 1/x
            n = -n
        return self.helper(x, n)

    def helper(self, x, n):
        if n == 0: return 1
        half = self.helper(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
    #O(logn), O(logn)


# Solution2.1: Recursion cleaner way
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return 1 / self.myPow(x, -n)
        half = self.myPow(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
    #O(logn), O(logn)