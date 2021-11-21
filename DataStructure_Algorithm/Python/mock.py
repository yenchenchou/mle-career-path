"""
408. Split Array Largest Sum
https://leetcode.com/problems/split-array-largest-sum/discuss/769701/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.

Given an array nums which consists of non-negative integers and an integer m, 
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Input: nums = [7,2,5,10,8], m = 2 
Output: 18


[1, 1, 2, 3] m=3
 1,1 |  2  | 3* : result 3

[7,2,5,10,8]
[0, 7, 9, 14, 24, 32]
"""



class Solution:
    def split_max(self, nums: List[int], m: int) -> int:
        # accumulated array to make it ordered
        accumulate_ls = [0].extend(nums)
        for i in range(1, len(nums)+1):
            accumulate_ls[i] += accumulate_ls[i-1]

        ...
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2
            split_point = self.split_array(mid)

    def split_array(self, val):
        pass


"""
2321

2[assa23[acc]]
assaaccaccassaaccacc


2[acs2[acc]]sxx2[sds]asdsad

curr = acc
str = [acsaccaccacsaccacc, sxx, sdssds]
num = []

curr = asdsad
times = 

tmp = 
  2
 / \

"""
# 394. Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        curr = ""
        for c in s:
            if c.isdigit():
                # k = k*10 + int(c)
                if curr.isalpha():
                    str_stack.append(curr)
                    curr = ""
                curr += c
            elif c == "[":
                num_stack.append(int(curr))
                curr = ""
            elif c == "]":
                if curr == "":
                    curr = str_stack.pop()
                    curr = str_stack.pop() + curr 
                times = num_stack.pop()
                tmp = curr * times
                str_stack.append(tmp)
                curr = ""
            elif c.isalpha():
                curr += c

        return "".join(str_stack) + curr




























