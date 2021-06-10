# 286. Walls and Gates

# Solution1: bfs + queue -> still taking too much time
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return None
        queue = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            for row, col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if (
                    0 <= i + row < len(rooms)
                    and 0 <= j + col < len(rooms[0])
                    and rooms[i + row][j + col] > rooms[i][j]
                ):
                    rooms[i + row][j + col] = rooms[i][j] + 1
                    queue.append((i + row, j + col))  # O(kmn), O(nm)


# Solution2: better speed and space
class Solution:
    def wallsAndGates2(self, rooms):
        # using index searh slower than no look up
        # q = [
        #     (i, j)
        #     for i in range(len(rooms))
        #     for j in range(len(rooms[0]))
        #     if not rooms[i][j]
        # ]

        q = [
            (i, j)
            for i, row in enumerate(rooms)
            for j, r in enumerate(row)
            if not r
        ]
        for i, j in q:
            for I, J in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if (
                    0 <= I < len(rooms)
                    and 0 <= J < len(rooms[0])
                    and rooms[I][J] > 2 ** 30
                ):
                    rooms[I][J] = rooms[i][j] + 1
                    q.append((I, J))