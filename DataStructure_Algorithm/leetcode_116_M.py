# 116. Populating Next Right Pointers in Each Node

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
    def connect(self, root: "Node") -> "Node":
        # observation: leverl order input, # for output right after the node
        # bfs
        # we need to use some way to let the us know which level is
        # we only point next to the nodes on the same level except for the right mode node
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


# Solution2: oprate the next pointer on the next level
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
    def connect(self, root: "Node") -> "Node":
        # observation
        # at level n ,have access to level n+1
        # we control the pointers of children and point to the next node
        # point to the node with sme parent
        # point to the node with different parent but same level
        # everytime, we start at the leftmost
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next

            leftmost = leftmost.left

        return root  # O(n), O(1)
