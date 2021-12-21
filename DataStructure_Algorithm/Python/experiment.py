# 1. pre, in ,post order traversal

# 2. 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        1. If I want to know the max depth, ask the left max depth and right max depth then compare
        2. Do the above repeatedly

             1
           /   \
          2     3    1 + max(0, 0)
         / \   / \
        nullnull null  

        Time: O(n) -> number of nodes 
        Space: O(n) -> max number of call stacks if extreme skewed
        """
        # base case
        if not root: return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return 1 + max(left_height, right_height)


# 3. How to determine whether the tree is balanced binary tree? (110. Balanced Binary Tree)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root)[1]
        
        
    def isBalancedHelper(self, root):
        """
        1. Know the definition of balanced, every left/right sub tree height diff <= 1
        2. How to know if balanced?
            -> get max height from left/right, if height diff > 1 then flag False
            -> the return value has height, boolean_flag
        
                1
               / \
              3   4    (3, F), 
             / \ / \
       (2,T)5  (0,T)
           / \
          7   1
         (1,T) (1,T)
        
        """
        # base case
        if not root: return 0, True
        
        left_h, left_balanced = self.isBalancedHelper(root.left)
        # this return will let the last stack (root level) release earlier and stop recusion process
        if not left_balanced:  
            return 0, False  # 0 can be left_h, it doesn't matter
        right_h, right_balanced = self.isBalancedHelper(root.right)
        # this return will let the last stack (root level) release earlier and stop recusion process
        if not right_balanced:
            return 0, False  # 0 can be right_h, it doesn't matter
        
        return 1 + max(left_h, right_h), abs(left_h - right_h) < 2


# 4. Determine whether a binary tree is symmretric
class Solution:
    def isSymmetric(self, root) -> bool:
        pass

# 5. Determine whether is identical, child rotation is allow

# 6. Determine a binary tree is BST 