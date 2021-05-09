# 1448. Count Good Nodes in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # left/right child is >= root then count
        if not root:
            return 0
        self.cnt = 0

        def helper(node, val):
            if not node:
                return None
            if node.val >= val:
                self.cnt += 1
            helper(node.left, max(node.val, val))
            helper(node.right, max(node.val, val))

        helper(root, root.val)
        return self.cnt  # O(n), O(n)
