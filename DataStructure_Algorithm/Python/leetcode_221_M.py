# 221. Maximal Square


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach
        if not matrix or len(matrix) == 0:
            return 0

        row, col = len(matrix), len(matrix[0])
        max_side = 0
        dp = [[0] * (col + 1) for _ in range(row + 1)]

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == "1":
                    dp[r + 1][c + 1] = (
                        min(dp[r][c], dp[r + 1][c], dp[r][c + 1]) + 1
                    )
                    max_side = max(max_side, dp[r + 1][c + 1])
        return max_side ** 2