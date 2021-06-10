# 346. Moving Average from Data Stream

# Solution: Use deque in Python
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.res = deque()

    def next(self, val: int) -> float:
        self.res.append(val)

        if len(self.res) > self.size:
            self.res.popleft()

        return sum(self.res) / len(
            self.res
        )  # O(m): sum calculation, O(n): size of the queue


# Solution2: Do the sum during the operation
class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.res = deque()
        self.windowSum = 0

    def next(self, val: int) -> float:
        self.res.append(val)
        if len(self.res) > self.size:
            minusBack = self.res.popleft()
        else:
            minusBack = 0
        self.windowSum = self.windowSum - minusBack + val

        return self.windowSum / len(self.res)  # O(1), O(n)
