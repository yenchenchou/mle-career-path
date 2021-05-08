# 117. Populating Next Right Pointers in Each Node II

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# Solution1: use queue to store the node for the current level and pop
# two loop> the outer one is resppnsible for visiting each level ,
# and the inner one is to handle the process in a particular level
from collections import deque


class Solution:
    def connect(self, root: "Node") -> "Node":
        # each level, handle of the next pointer
        # queue =
        # [1,2,3]
        if not root:
            return root
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
        return root  # O(n), O(n)


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def process(self, childNode, prev, leftmost):
        if childNode:
            if prev:
                prev.next = childNode
            else:
                leftmost = childNode
            prev = childNode
        
        return prev, leftmost
    
    
    def connect(self, root: 'Node') -> 'Node':
        # each level, handle of the next pointer
        # queue = 
        # [1,2,3]
        if not root: return root
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = self.process(curr.left, prev, leftmost)
                prev, leftmost = self.process(curr.right, prev, leftmost)
                curr = curr.next
        return root