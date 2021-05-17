# 114. Flatten Binary Tree to Linked List
# Solution1: recurion and start from the bottom
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        # do preorder travers and start from the bottom
        #
        if not root:
            return root
        if not root.left and not root.right:
            return root
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        if left:
            left.right = root.right
            root.right = root.left
            root.left = None
        return right if right else left


# Solution2: use dfs still but use stack



# Jack's Solution
"""
Given the root of a binary tree, flatten the tree into a "linked list":

    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]


Input: 


Follow up: Can you flatten the tree in-place (with O(1) extra space)?

"""

import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_flatten():
    """
    root = [1, 2 ,3]
    output: [1, null, 2, null, 3]
    """
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)
    exp = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    s = Solution()
    s.flatten(root)
    cur = root
    while cur:
        cur = cur.right
        
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    stack = deque()
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # Input: root = [1,2,5,3,4,null,6]
        # Output: [1,null,2,null,3,null,4,null,5,null,6]
        
        def helper(node):
            if not node:
                return None
            
            right = helper(node.right)
            left = helper(node.left)

            if right:
                self.stack.append(right)
            if left:
                self.stack.append(left)
            self.stack.append(node)
            # # return self.stack
        
        # stack = [6, 5, 4, 3, 2]
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6
        helper(root)
        while self.stack:
            node = self.stack.pop()
            node.left = None
            if self.stack:
                node.right = self.stack[-1]

        return root
        
        
        
        
pytest.main()
        
        
        
        
        
        