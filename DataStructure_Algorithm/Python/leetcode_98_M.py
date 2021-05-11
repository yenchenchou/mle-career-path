# 98. Validate Binary Search Tree

# Solution1: Recursive
# the node should be : left.val < node.val < right.val
# inorder traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        return self.helper(root, low=float("inf"), high=float("-inf"))

    def helper(self, node, low, high):
        if not node:
            return True
        if node.val >= low or node.val <= high:
            return False
        # left = self.helper(node.left, min(node.val, low), high)
        # right = self.helper(node.right, low, max(node.val, high))
        # return left and right  # O(n), O(n)
        return self.helper(
            node.left, min(node.val, low), high
        ) and self.helper(
            node.right, low, max(node.val, high)
        )  # O(n), O(n)


# Solution1.2
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        return self.helper(root, low=float("-inf"), high=float("inf"))

    def helper(self, node, low, high):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False

        return self.helper(node.right, node.val, high) and self.helper(
            node.left, low, node.val
        )


# Solution2.1: Iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float("inf"), float("-inf"))]
        while stack:
            # [4,1,5, null, null, 3, 7]
            node, low, high = stack.pop()
            val = node.val
            if val >= low or val <= high:
                return False
            if node.right:
                stack.append((node.right, low, max(high, val)))
            if node.left:
                stack.append((node.left, min(low, val), high))
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            # [4,1,5, null, null, 3, 7]
            node, low, high = stack.pop()
            val = node.val
            if val <= low or val >= high:
                return False
            if node.left:
                stack.append((node.left, low, val))
            if node.right:
                stack.append((node.right, val, high))
        return True
