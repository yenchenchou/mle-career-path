# 938. Range Sum of BST

# Solution1: use dfs, this method applies to whether it is a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans = 0

        def helper(node):
            if not node:
                return 0
            if low <= node.val <= high:
                self.ans += node.val
            helper(node.left)
            helper(node.right)

        helper(root)
        return self.ans


# Solution1.2: consider the property of BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans = 0

        def helper(node):
            if not node:
                return 0
            if low <= node.val <= high:
                self.ans += node.val
            if node.val > low:
                helper(node.left)
            if node.val < high:
                helper(node.right)

        helper(root)
        return self.ans


# Solution2: Iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if node.val > L:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans
