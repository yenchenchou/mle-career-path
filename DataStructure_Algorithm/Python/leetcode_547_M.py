# 547. Number of Provinces
# SOlution1: loop on each row and dfs on that row
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set()

        def dfs(row):
            for i, adj in enumerate(isConnected[row]):
                if adj and i not in visited:
                    visited.add(i)
                    dfs(i)

        for row in range(len(isConnected)):
            if row not in visited:
                dfs(row)
                res += 1

        return res
        # [[1,1,0],[1,1,0],[0,0,1]]
        # [[1,0], [0,1]]
