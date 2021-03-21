from queue import Queue

# There are three k=types of queue in total
# 1. FIFO
# 2. LIFO like a stack
# 3. Priority queue the entries are kept sorted (using the heapq module) and the lowest valued entry is retrieved first.

# Reference link: https://docs.python.org/3/library/queue.html
obj = Queue(maxsize=2)
obj.put(1)  # this action is called enqueue
obj.put(3)
print(obj.full())
print(obj.put(4, block=True, timeout=10))
print(obj.get())
print(obj.put(4, block=False))
print(obj)