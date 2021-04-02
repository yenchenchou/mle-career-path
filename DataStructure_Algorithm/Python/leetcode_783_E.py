# 783. Minimum Distance Between BST Nodes
# Soluion1: Iteration

# Solution2: Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(node):
            if not node: return None
            dfs(node.left)
            self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            dfs(node.right)
        self.ans = float("inf")
        self.prev = float("-inf")
        dfs(root)
        return self.ans
        