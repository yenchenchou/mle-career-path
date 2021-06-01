# 589. N-ary Tree Preorder Traversal

# Solution1: recursion
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if not node:
            return None
        res.append(node.val)
        for child in node.children:
            self.dfs(child, res)

# Solution2: Iteratiion
