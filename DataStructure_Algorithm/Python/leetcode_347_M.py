# 347. Top K Frequent Elements
# Solution1: Counter by negative num to create max heap + push top k to result
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = -1
            else:
                dic[num] -= 1
        dic = [(val, key) for key, val in dic.items()]
        heapq.heapify(dic)
        res = []
        for _ in range(k):
            val = heapq.heappop(dic)[1]
            res.append(val)
        return res


# Solution1.2: Counter + use nlargest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        dic = [(val, key) for key, val in dic.items()]
        heapq.heapify(dic)
        return [key for val, key in heapq.nlargest(k, dic)]  # O(nlogk), O(n)
