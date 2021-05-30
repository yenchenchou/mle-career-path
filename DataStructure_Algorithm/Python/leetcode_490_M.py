"""
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.

Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false

"""
# 490. The Maze

from collections import deque


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        visited[start[0]][start[1]] = True

        queue = deque([start])
        while queue:
            curr = queue.popleft()

            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True

            for path in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
                row = curr[0] + path[0]
                col = curr[1] + path[1]

                while (
                    0 <= row < len(maze)
                    and 0 <= col < len(maze[0])
                    and maze[row][col] == 0
                ):
                    row += path[0]
                    col += path[1]

                new_row = row - path[0]
                new_col = col - path[1]

                if not visited[new_row][new_col]:
                    queue.append((new_row, new_col))
                    visited[new_row][new_col] = True

        return False
