"""
378. Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.


Example 1:

Input: matrix = [
    [1,5,9],
    [10,11,13],
    [12,13,15]
    ], 
    k = 8 Output: 13 Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Constraints:

n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

"""

from types import List
from collections import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        h = []
        for i in range(min(k, n)):
            h.append((matrix[i][0], i, 0))
        heapq.heapify(h)

        while k != 0:
            val, row, col = heapq.heappop(h)
            if col < n - 1:
                heapq.heappush(h, (matrix[row][col+1], row, col + 1))
            k -= 1
        return val