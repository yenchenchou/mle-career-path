# 452. Minimum Number of Arrows to Burst Balloons
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # interval -> stack / queue / sort
        # [[1,6], [2,8], [7,12], [10,16]]
        # [[1,6], [2,3], [3,4]]
        # [[1,6], [2,5], [4,6]]
        #  when the first of next pair is cur >= first and cur <= second
        # first time 20 mins to complete
        points.sort()
        stack = [points[0]]
        for x1, x2, in points[1:]:
            if stack[-1][1] >= x1 and stack[-1][1] > x2:
                stack[-1][1] = x2
            elif stack[-1][1] < x1:
                stack.append([x1, x2])
        return len(stack)  # O(nlogn), O(n)


# Solution2: This method will apply on #253 Meeting rooms II
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        stack = []
        maxVal = tmp = 0
        for start, end in intervals:
            stack.append([start, 1])
            stack.append([end, -1])

        for t, i in sorted(stack):
            tmp += i
            maxVal = max(maxVal, tmp)
        return maxVal
