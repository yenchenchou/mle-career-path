#113. Path Sum II

"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Input: root = [1,2,3], targetSum = 5
Output: []

Input: root = [1,2], targetSum = 0
Output: []

Input: root = [], targetSum = 10
Output: []

"""

# Input: root = [1, 2, 3, 4, null, 6, 3], targetSum = 7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root: return []
        
        if not root.left and not root.right:
            if targetSum == root.val:
                return [[root.val]]
            else:
                return []
        result = self.pathSum(root.left, targetSum - root.val) + \
        self.pathSum(root.right, targetSum - root.val)
        return [[root.val] + val for val in result]  #