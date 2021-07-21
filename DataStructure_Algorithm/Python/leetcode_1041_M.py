# 1041. Robot Bounded In Circle


# Solution1: One pass with fixed order of the directions
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
                     #north,   east,   south,   west
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = d = 0
        for val in instructions:
            if val == "G":
                x += directions[d][0]
                y += directions[d][1]
            elif val == "L":
                d = (d + 3) % 4
            elif val == "R":
                d = (d + 1) % 4
        return (x == 0 and y == 0) or d != 0  # O(n), O(1)
