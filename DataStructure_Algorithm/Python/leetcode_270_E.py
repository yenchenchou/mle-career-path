# 270. Closest Binary Search Tree Value

# Solution1: Iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack = [root]
        diff = float("inf")
        while stack:
            node = stack.pop()
            if abs(node.val - target) < diff:
                diff = abs(node.val - target)
                res = node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res   
    # [1]:2, [1,2]:2, [4,2,6]:3
    # O(n), O(1)


# Solution2: Iteration but less time complexity: use prev to cache the previous node value
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        prev = root.val
        while root:
            if abs(root.val - target) < abs(prev - target):
                prev = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return prev  # [1], [1,2]:3, [4,2,6,1,3]:1

    # O(logn), O(1)


# Solution3: Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        prev = float("inf")
        return self.helper(root, target, prev)

    def helper(self, root, target, prev):
        if not root:
            return prev

        if abs(prev - target) > abs(root.val - target):
            prev = root.val

        if root.val > target:
            return self.helper(root.left, target, prev)
        else:
            print(prev)
            return self.helper(root.right, target, prev)

    # O(logn), O(n)-> unbalanced tree
