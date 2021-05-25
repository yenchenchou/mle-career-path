# 695. Max Area of Island

# Solution1.1: linear search and dfs, use a set seen where the algorithm has visited


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxNum = 0
        row, col = len(grid), len(grid[0])
        seen = set()

        def dfs(i, j):
            if (
                i < 0
                or j < 0
                or i >= row
                or j >= col
                or ((i, j) in seen or grid[i][j] == 0)
            ):
                return 0
            # grid[i][j] = 0
            seen.add((i, j))
            return (
                1
                + dfs(i + 1, j)
                + dfs(i - 1, j)
                + dfs(i, j + 1)
                + dfs(i, j - 1)
            )

        for i in range(row):
            for j in range(col):
                num = dfs(i, j)
                maxNum = max(maxNum, num)
        return maxNum  # O(m*n), O(m*n)


# Solution1.2: linear search and dfs, assign the visited location to zero to prevent next time step in
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxNum = 0
        row, col = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return (
                1
                + dfs(i + 1, j)
                + dfs(i - 1, j)
                + dfs(i, j + 1)
                + dfs(i, j - 1)
            )

        for i in range(row):
            for j in range(col):
                num = dfs(i, j)
                maxNum = max(maxNum, num)
        return maxNum  # O(m*n), O(m*n)
