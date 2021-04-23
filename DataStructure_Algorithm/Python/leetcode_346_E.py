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

        return sum(self.res) / len(self.res)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)