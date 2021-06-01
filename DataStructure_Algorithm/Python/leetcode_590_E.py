# 590 N-ary Tree Postorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if not node:
            return None
        for child in node.children:
            self.dfs(child, res)
        res.append(node.val)