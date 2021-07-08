# On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

# Input: instructions = "GGLLGG"

# Output: true
# LLLL
# RRRR
# Input: instructions = "GG"
# Output: false
# Explanation: The robot moves north indefinitely.

# Input: instructions = "GL"
# Output: true
#  (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


# LRGGGR
# (0, 0) -> (0, 3) -> (3, 3) -> (3, 0) -> (0, 0)

# LLLLLRRRRRR

# GL


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 0=north, 1=left, 2=south, 3=right
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        i = 0
        x, y = 0, 0
        for val in instructions:
            if val == "G":
                x += directions[i][0]  #
                y += directions[i][1]  #
            elif val == "L":
                i = (i + 1) % 4  #
            else:
                i = (i + 3) % 4
        return (x == 0 and y == 0) or i != 0
        # dic = {"G":0, "L":0, "R":0}
        # for char in instructions:
        #     dic[char] += 1

        # if dic["L"] == 0 and dic["R"] == 0:
        #     return False
        # elif dic["L"] == dic["R"] and dic["G"] != 0:
        #     return False
        # else:
        #     return True