# 252. Meeting Rooms


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        if len(intervals) < 2:
            return True
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


# O(nlogn) -> sorting, O(1)
