# 779. K-th Symbol in Grammar
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1 return 0
        half = 2 ** (N-2)
        if K <= half:
            return self.kthGrammar(N-1, K)
        else:
            res = self.kthGrammar(N-1, K-half)
            return 1 if res == 0 else 1
    #O(n), O(n)