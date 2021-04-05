# 250. Count Univalue Subtrees

# Solution1: define what is uni-value and write out some easy test and observation
# think about base case
# think about how to write the recursive function: what to pass to the parent node
# does pre/in/post/level order benfit me?
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        return self.helper(root)[0]

    def helper(self, node):
        if not node:
            return 0, True
        if not node.left and not node.right:
            return 1, True
        left, flag1 = self.helper(node.left)
        right, flag2 = self.helper(node.right)
        if flag1 and flag2:
            if node.left and node.left.val != node.val:
                return left + right, False
            if node.right and node.right.val != node.val:
                return left + right, False

            return 1 + left + right, True
        return left + right, False


# Solution1.2: Still pass the info to parent node but we use instance variables instead


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.cnt = 0
        self.dfs(root, None)
        return self.cnt

    def dfs(self, node, parentNode):
        if not node:
            return True
        left = self.dfs(node.left, node.val)
        right = self.dfs(node.right, node.val)
        if left and right:
            self.cnt += 1
        return left and right and node.val == parentNode