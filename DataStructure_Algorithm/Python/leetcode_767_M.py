# 767. Reorganize String
# Solution1: Priority queue

from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        # what condition are we able to reorganize:
        # "aaabbb" -> "ababab"
        # "aabbbb" ->  False
        # "aabbc" -> "ababc"
        # "aabbccd" -> "abcdabc"
        # "aaaabcd" -> abacada
        # When none of the distinct strings has > len(S)//2 counts
        pq = [(-val, key) for key, val in Counter(S).items()]
        heapq.heapify(pq)
        res = []
        preva, prevb = 0, ""
        while pq:
            a, b = heapq.heappop(pq)
            res.append(b)
            if preva < 0:
                heapq.heappush(pq, (preva, prevb))
            a += 1
            preva, prevb = a, b
        res = "".join(res)
        if len(res) != len(S):
            return ""
        return res
