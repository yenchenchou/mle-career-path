# 118. Pascal's Triangle

# Solution1: Iteration
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        if numRows == 1: return [[1]]
        if numRows == 2: return res
        for i in range(2, numRows):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row)-1):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res #[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    #O(n^2), O(n^2)


# Solution1.2: Iteration
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1: return res
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(res[i-1][j-1] + res[i-1][j])
            row.append(1)
            res.append(row)
        return res #[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]