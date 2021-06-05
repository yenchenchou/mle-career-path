# 733. Flood Fill
# Solution1: dfs


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        row, col = len(image), len(image[0])
        curColor = image[sr][sc]
        if curColor == newColor:
            return image

        def dfs(r, c):
            if image[r][c] == curColor:
                image[r][c] = newColor
                if r > 0:
                    dfs(r - 1, c)
                if r < row - 1:
                    dfs(r + 1, c)
                if c > 0:
                    dfs(r, c - 1)
                if c < col - 1:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image
