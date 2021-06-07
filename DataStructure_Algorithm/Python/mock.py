"""
You are given an m x n integer matrix heights representing the height of each unit cell in a continent. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges.

Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height.

Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.

https://assets.leetcode.com/uploads/2021/03/26/ocean-grid.jpg

Input: heights = [[1,2,2,3,5],
                  [3,2,3,4,4],
                  [2,4,5,3,1],
                  [6,7,1,4,5],
                  [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]


Input: heights = [[2,1],
                  [1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def is_pacific(row, col):
            return True if col < 0 or row < 0 else False
        
        def is_atlantic(row, col):
            return True if col >= len(heights) or row >= len(heights[0]) else False

        def helper(row, col, visited, to_oceans):
            visited.add((row, col))

            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + x, col + y 
                if not (new_row, new_col) in visited:
                    if is_pacific(new_row, new_col):
                        to_oceans[0] = True
                    elif is_atlantic(new_row, new_col):
                        to_oceans[1] = True
                    elif heights[row][col] >= heights[new_row][new_col]:
                        helper(new_row, new_col, visited, to_oceans)
        
        result = []
        for row in range(len(heights)):
            for col in range(len(heights[row])):
                visited = set()
                # to_pacific, to_atlantic
                to_oceans = [False, False]
                helper(row, col, visited, to_oceans)
                if all(to_oceans):
                    result.append((row, col))
        
        return result
