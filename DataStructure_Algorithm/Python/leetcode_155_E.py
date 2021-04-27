class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # use two stacks to implement
        # first stack as normal stack
        # second stack to keeo track of min value each time
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins:
            self.mins.append(val)
        elif self.mins[-1] >= val:
            self.mins.append(val)
        self.stack.append(val)
        # 10, 2, 3, 4, 1
        # 10, 2, 1

    def pop(self) -> None:
        if self.mins[-1] == self.stack[-1]:
            self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()