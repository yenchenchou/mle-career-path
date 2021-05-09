# 235. Lowest Common Ancestor of a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return root
        node = root
        q_val, p_val = q.val, p.val
        while node:
            if q_val < node.val and p_val < node.val:
                node = node.left
            elif q_val > node.val and p_val > node.val:
                node = node.right
            else:
                return node  # O(n), O(1)
