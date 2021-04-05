# 102. Binary Tree Level Order Traversal

# Solution 1: Iteration with Queue. Use Queue to measure whether we visit all the nodes at the same time,
# store the value into res as long as we reach the value. In order to have the level sublist, create a level
# as level counter. Hence, we can insert value to the empty sublist by index

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue, res = Queue(), []
        queue.put(root)
        level = 0
        while queue.qsize() != 0:
            res.append([])
            for i in range(queue.qsize()):
                node = queue.get()
                res[level].append(node.val)
                if node.left: 
                    queue.put(node.left)
                if node.right: 
                    queue.put(node.right)
            level += 1
        return res  # O(n), O(n), [], [1], [1,2,null,3], [1,2,3,null,4]

# Solution 2: Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.helper(root, res, level=0)
        return res
    
    def helper(self, node, res, level):
        if not node: return None
        if len(res) == level:
            res.append([])
        res[level].append(node.val)
        if node.left: self.helper(node.left, res, level+1)
        if node.right: self.helper(node.right, res, level+1)