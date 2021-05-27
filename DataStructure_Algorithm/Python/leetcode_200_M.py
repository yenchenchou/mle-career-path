# 200. Number of Islands

# Solution1: linear scan + dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # linear scan and dfs
        # once it start dfs, assign all the connected part to "0"
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        row, col = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)  # O(mn), O(mn)
