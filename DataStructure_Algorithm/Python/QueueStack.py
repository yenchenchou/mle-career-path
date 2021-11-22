"""
As long as it follows the logic LIFO or FIFO, you can call them Stack or Queue. 
You can use array, list, or LinkedList ...etc to implement. Stack or Queue are just a concepts.

It's very rare to ask solely on Stack or Queue. It come with other data structures at the same time.

Common problems for Queue/Stack
1. Fix window size sliding window
2. Floating size sliding window
3. Use Stack implement Queue, Deque
"""
# 1. How to implement a queue by using two stacks(please describe it)
#232. Implement Queue using Stacks


# 2. How to implement the min() function, when using 2 stacks or ine stack one hash map with time complexity
# follow up, minimize duplicate store in stack / hash map!!
# note that it's impossible to do that with one stack, so multiple stacks mix with other data structure is possible
# 155. Min Stack

# 3. Sort number with two stack, the input has no duplicates and all are int -> Use selection sort concept
# Follow up: if it has duplicte and the value is float
    # use a counter until counter minus to 0



# 4. How to use multiple stacks to implement a deque. Prefer O(1) amortized time for all operations
# three stacks
class Deque:
    def __init__(self):
        # one handle front and the front elements go to tmp first, the other handle back, tmp for restructure and transition for front
        # 1. when front input, push to tmp one by one, then pop one by one to front
        # 2. when end input, push to end and serve it self
        # 3. when front is empty but call front, end split half to tmp + end remain to front + tmp back to end, 
        # 4. when end is empty but call end, front split half to tmp + front remain to end + tmp back to front
        self.tmp = [] 
        self.front = []  # handle back, append back can also handle back
        self.end = []

    def popLeft(self):
        if not self.front:
            for i in range(len(self.end)//2+1):
                self.tmp.append(self.end.pop())
            while self.end:
                self.front.append(self.end.pop())
            while self.tmp:
                self.end(self.tmp.pop())
        else:
            return self.front.pop()

    def popRight(self):
        if not self.end:
            for i in range(len(self.front)//2+1):
                self.tmp.append(self.front.pop())
            while self.front:
                self.end.append(self.front.pop())
            while self.tmp:
                self.front.append(self.tmp)
        else:
            return self.end.pop()

    def appendLeft(self, val):
        self.tmp.append(val)
        while self.tmp:
            self.front.append(self.tmp.pop())

    def appendRight(self, val):
        self.end.append(val)

    def getSize(self):
        return len(self.getDeque())

    def getDeque(self):
        return self.front + self.end


def test1():
    # [3,1,6]
    deque = Deque()
    deque.appendLeft(1)
    deque.appendLeft(3)
    deque.appendRight(6)
    deque.popLeft()
    deque.popRight()
    print(deque.getDeque())
    assert deque.getDeque() == [1], "Should be [1]"


def test2():
    # [1]
    deque = Deque()
    deque.appendLeft(1)
    deque.appendLeft(1)
    deque.appendLeft(1)
    deque.popRight()
    deque.popRight()
    deque.popRight()
    assert deque.getDeque() == [], "Should be []"


def test3():
    # [3,1]
    deque = Deque()
    deque.appendLeft(1)
    deque.appendLeft(3)
    deque.popLeft()
    deque.popRight()
    assert deque.getSize() == 0, "Should be 0"


test1()
test2()
# test3()
# When to use stack? When you need to look at the latest value of the left side 