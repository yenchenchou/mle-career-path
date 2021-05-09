# 451. Sort Characters By Frequency

# Solution 1: Counter -> heapify with key value reverse -> pop and concat
from collections import Counter
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        # return "".join(sorted(s, reverse=False))
        # clarify: # of counts, "a" > "A" and "b" > "a"
        # Counter -> heapify with key value reverse -> pop and concat
        res = []
        s = Counter(s)
        s = [(-val, key) for key, val in s.items()]
        heapq.heapify(s)
        # Sort and Build string
        while s:
            val, key = heapq.heappop(s)
            res.append(-val * key)
        return "".join(res)


# Solution2: Bucket Sort