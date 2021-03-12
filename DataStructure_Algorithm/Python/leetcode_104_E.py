#104. Maximum Depth of Binary Tree

# Solution1: Iteration DFS by saving the depth and the node in the stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        depth = 0
        while stack != []:
            node, curdepth = stack.pop()
            if node:
                depth = max(curdepth, depth)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return depth
    # O(n), O(n): worst case when node only has left/right clild


# Solution1.2: recursive DFS 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
    #O(n), O(n) -> on average O(logn)