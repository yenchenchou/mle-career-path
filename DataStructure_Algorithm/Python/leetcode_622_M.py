# 622. Design Circular Queue
class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.enIndex, self.deIndex = 0, 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.enIndex] = value
        self.enIndex = (self.enIndex + 1) % len(self.queue)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.deIndex] = None
        self.deIndex = (self.deIndex + 1) % len(self.queue)
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.deIndex]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.enIndex - 1]

    def isEmpty(self) -> bool:
        return self.enIndex == self.deIndex and not self.queue[self.deIndex]

    def isFull(self) -> bool:
        return self.enIndex == self.deIndex and self.queue[self.deIndex]


# [1,2]
# . e
#  d


# [None, None]
#  e
# . d


# Solution1.2: more intuitive but a bit redundant
class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.enIndex, self.deIndex = 0, 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.enIndex] = value
        self.size += 1
        self.enIndex = (self.enIndex + 1) % len(self.queue)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.deIndex] = None
        self.size -= 1
        self.deIndex = (self.deIndex + 1) % len(self.queue)
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.deIndex]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.enIndex - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()