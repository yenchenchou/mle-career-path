# 236. Lowest Common Ancestor of a Binary Tree

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
        # find p and q
        # 1. share the same parent, then the parent is LCA
        # 2. one is the parent and the other is left/right child, then the parentLCA
        # 3. diff parents
        # bottom up-> dfs
        if not root:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left or right
        # if not left:
        #     return right
        # if not right:
        #     return left
