"""
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are super-palindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.

Example 2:

Input: left = "1", right = "2"
Output: 1

Constraints:
    1 <= left.length, right.length <= 18
    left and right consist of only digits.
    left and right cannot have leading zeros.
    left and right represent integers in the range [1, 1018].
    left is less than or equal to right.

(1, 1)
(2, 4)
(3, 9)
(11, 121)
(22, 484)
(101, 10201)  
(111, 12321)
(121, 14641)
(202, 40804)
(212, 44944)
(1001, 1002001)
(1111, 1234321)
(2002, 4008004)


21012, 

12021 
22022


"""

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        candidants, cnt = [], 0
        for val in range(int(left), int(right)+1):
            if val ** 2 <= int(right)+1:
                candidants.append(val)

        for val in candidants:
            if str(val) == str(val)[::-1]:
                cnt += 1
        
        return cnt