# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val == r.val:
                stack.append((l.left, r.right))
                stack.append((l.right, r.left))
            else:
                return False
        return True


# Solution2: Recursion
# The point of this question is to think when the tree is symmetric?
# same valuie of each left sub tree is a mirror reflection of the right sub tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.helper(root.left, root.right)

    def helper(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val == r.val:
            out1 = self.helper(l.left, r.right)
            out2 = self.helper(l.right, r.left)
            return out1 and out2