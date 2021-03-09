# 119. Pascal's Triangle II (See the anwer again)

# Solution1: Same as prob 118
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # [1]
        # [1, 1]
        # [1, 2, 1]
        # [1, 3, 3, 1]
        res = [1]
        if rowIndex == 0: return res
        for i in range(1, rowIndex+1):
            row = [1]
            for j in range(1, i):
                row.append(res[i-1][j-1] + res[i-1][j])
            row.append(1)
            res.append(row)
        return res[rowIndex]
    #O(n^2), O(n^2)