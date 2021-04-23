class Queue:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.empty():
            return None
        item = self._items[0]
        self._items.pop(0)
        return item

    def empty(self):
        return len(self._items) == 0

    def front(self):
        if self.empty():
            return None
        return self._items[0]


q = Queue()
q.enqueue(3)
print(q.front())
