class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # how to keep track of max, two stack -> one save the max values
        # problem for two stacks: #[2,4,1], [2,4] -> the structure will disturb by popMax -> O(n) to move -> need to arrange two stack every time
        # test1: [5,1,7,5], maxx:[5, 7]
        # test2 [5,3,1], [5]
        self.stack = []

    def push(self, x: int) -> None:
        curMax = x
        if self.stack: curMax = max(self.peekMax(), x)
        self.stack.append((x, curMax))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        # [(5,5), (3,5), (1,5)]
        buffer, curMax = [], self.stack[-1][1]
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == curMax:
                break
            else:
                buffer.append(self.pop())
        print(self.pop())
        while buffer:
            self.push(buffer.pop())
        return curMax


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

#1. More reading: https://leetcode.com/problems/max-stack/discuss/309621/Python-using-stack-%2B-heap-%2B-set-with-explanation-and-discussion-of-performance
#2. https://leetcode.com/problems/max-stack/solution/