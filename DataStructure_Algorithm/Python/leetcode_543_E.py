# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.depth(root)
        return self.diameter

    def depth(self, root):
        if not root:
            return 0
        left_height = self.depth(root.left)
        right_height = self.depth(root.right)
        self.diameter = max(self.diameter, left_height + right_height)
        return 1 + max(left_height, right_height)