class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [(5, 5), (3, 5), (1, 5)]

    def printresult(self):
        print(self)
        print(self.pop())
m = MaxStack()
print(m.printresult())