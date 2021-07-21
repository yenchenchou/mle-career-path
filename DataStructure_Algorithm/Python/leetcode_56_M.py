# 56. Merge Intervals
# sort the first element of each sublist
# compare the last index of the last sublist store in the answer
# if the value is smaller than the first index value in the current iteration sublist
# we store into result
# if the sublist is overllaped, we meed to modify the last index of the sublist that under comparison
from random import randrange
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda x: x[0], reverse=False)
        intervals = self.quicksort(intervals)
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
    
    def quicksort(self, intervals):
        self.helper(intervals, 0, len(intervals)-1)
        return intervals
    
    def helper(self, intervals, start, end):
        if start >= end: return None
        pivotIndex = randrange(start, end+1)
        newIndex = self.partition(intervals, start, end, pivotIndex)
        self.helper(intervals, start, newIndex-1)
        self.helper(intervals, newIndex+1, end)
        
    def partition(self, intervals, start, end, pivotIndex):
        intervals[end], intervals[pivotIndex] = intervals[pivotIndex], intervals[end]
        newIndex = start
        for i in range(start, end):
            if intervals[i] < intervals[end]:
                intervals[i], intervals[newIndex] = intervals[newIndex], intervals[i]
                newIndex += 1
        intervals[end], intervals[newIndex] = intervals[newIndex], intervals[end]
        return newIndex

#O(n^2), O(n) -> store answer


# Solution2: self answer
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        # [[1,4],[4,5], [6,8]]
        stack = [intervals[0]]
        for i, j in intervals[1:]:
            if i <= stack[-1][-1] <= j:
                stack[-1][-1] = j
            elif stack[-1][-1] < i:
                stack.append([i, j])
        return stack


# Solution3: A little better
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        # [[1,4],[4,5], [6,8]]
        stack = []
        for i, j in intervals:
            if not stack or stack[-1][-1] < i:
                stack.append([i, j])
            else:
                stack[-1][-1] = max(stack[-1][-1], j)
        return stack
