# 560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # by oberservation, we notice that when the accumulated sum increas by k
        # then there is one or more Subarrays.
        # Also, we use dict to store the previous count of subarray sums
        dic = {0: 1}
        res = cnt = 0
        for val in nums:
            res += val
            cnt += dic.get(res - k, 0)
            dic[res] = dic.get(res, 0) + 1
        return cnt
