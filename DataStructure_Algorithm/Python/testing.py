"""
Count the number of prime numbers less than a non-negative number, n. 

Example 1:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
    Input: n = 0
    Output: 0

Example 3:
    Input: n = 1
    Output: 0 

Constraints:
    0 <= n <= 5 * 106

Hint #4  
    The Sieve of Eratosthenes is one of the most efficient ways to find all prime numbers up to n. 
    But don't let that name scare you, I promise that the concept is surprisingly simple.
    https://leetcode.com/static/images/solutions/Sieve_of_Eratosthenes_animation.gif

"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        ans = 0
        for val in range(2, n):
            ans += self.isPrime(val)
        return ans

    def isPrime(self, val):
        for i in range(2, int(val**0.5)+1):
            if val % i == 0:
                return 0
        return 1

class Solution():
    def countPrime(self, n) -> int:
        # n = 10, 4 -> 2, 3, 5, 7
        # n = 20, 8 -> 2, 3, 5, 7, 11, 13, 17, 19
        # n = 30, 10 -> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
        # n = 40, 12 -> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
        # count = 0
        # if n <= 1:
        #     return count
        # base_prime = [2, 3, 5, 7]
        # nonPrime = []
        count = 0
        # 2, 3, 4, 5 ... 10
        is_prime = [False for _ in range(n)]
        for i in range(2, n):
            if is_prime[i] == False:
                count += 1
                j = 2
                while i * j < n:
                    is_prime[i * j] = True
                    j += 1
        return count
