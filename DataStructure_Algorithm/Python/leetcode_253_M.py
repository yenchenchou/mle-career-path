# 253. Meeting Rooms II

# Solution1:  Chronological Ordering
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort the start time, but not enough
        # sort the end time as well
        # we give one pointer for start time and count # of rooms need, at the same time we set a counter start from 0, we let the counter += 1 by default unless we have empty room
        # when the current start time is >= end time then we know there is vaccancy
        # then we do counter -1
        # return the counter

        if not intervals:
            return 0
        counter, start, end = 0, 0, 0
        startTimes = sorted([val[0] for val in intervals])
        endTimes = sorted([val[1] for val in intervals])
        while start < len(intervals):
            if startTimes[start] >= endTimes[end]:
                counter -= 1
                end += 1
            counter += 1
            start += 1
        return counter


# O(nlogn) -> sorting, O(n)-> size N array

# Solution2: Priority queues
# let's dry run first, we found that sorting the starting is the start to do the comparison
# Also, we are not interested in which room is empty, it works as long as it is empty
# So, we use min heap to implement the priority queue. 
# Everytime we just check whether the new comming meeting has overlap with the top of the minheap
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(res, intervals[0][1])
        for session in intervals[1:]:
            if res[0] <= session[0]:
                heapq.heappop(res)
            heapq.heappush(res, session[1])
        return len(res)  # O(nlogn), O(n)
