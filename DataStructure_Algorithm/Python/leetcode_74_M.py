# 74. Search a 2D Matrix

# Solution1: Iteration
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)*len(matrix[0]) - 1
        while left <= right:
            mid = (right-left)//2 + left
            rowIndex = mid // len(matrix[0])
            colIndex = mid % len(matrix[0])
            num = matrix[rowIndex][colIndex]
            if num == target:
                return True
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
    # O(logn*m) #O(1)

# Solution2: Recursion