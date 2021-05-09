# 692. Top K Frequent Words

# Solition1: Sort

# Solution 2: Counter + heapify with max heap -> NOTE: the concept is right but answer is wrong -> forget alphabetical order!!
# pop the top k to res
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        cnt = [(-val, key) for key, val in cnt.items()]
        heapq.heapify(cnt)
        res = []

        for _ in range(k):
            val = heapq.heappop(cnt)[1]
            res.append(val)
        return res


# Solution 2.2:
