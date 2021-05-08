# 112. Path Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )
        # [1,2,3]:target=3


# O(n), O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, targetSum - root.val)]
        while stack:
            node, curSum = stack.pop()
            if not node.left and not node.right and curSum == 0:
                return True
            if node.left:
                stack.append((node.left, curSum - node.left.val))
            if node.right:
                stack.append((node.right, curSum - node.right.val))
        return False


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, targetSum - root.val)]  # remember to minus the root val
        while stack:
            node, targetSum = stack.pop()
            if node.left:
                stack.append((node.left, targetSum - node.left.val))
            if node.right:
                stack.append((node.right, targetSum - node.right.val))
            if not node.left and not node.right and targetSum == 0:
                return True
        return False