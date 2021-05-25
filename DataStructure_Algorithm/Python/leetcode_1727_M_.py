# 1727. Largest Submatrix With Rearrangements
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]
            cur = sorted(matrix[i], reverse=True)
            for j in range(len(matrix[0])):
                res = max(res, (j + 1) * cur[j])
        return res
