# 487. Max Consecutive Ones II
# Solution 1: cur array compare with prev array
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = cur = 0
        prev = -1  # never seen 0 before
        for val in nums:
            if val == 1:
                cur += 1
            else:
                prev, cur = cur, 0
            maxLen = max(maxLen, prev + 1 + cur)
        return maxLen  # O(n),  O(1)


# Solution2: Sliding window 
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # [1,0,1,1,0]
        slow = fast = maxlen = flag = 0
        while fast < len(nums):
            if nums[fast] == 0:
                flag += 1
            while flag == 2:
                if nums[slow] == 0:
                    flag -= 1
                slow += 1

            maxlen = max(maxlen, fast-slow+1)
            fast += 1
        return maxlen
