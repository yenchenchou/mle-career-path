# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
        # [3(tail of right), 9(head of left), 20(right child of 3), ]
        #

        def helper(inorder, postorder):
            if not inorder or not postorder:
                return None
            root = TreeNode(postorder.pop())
            div = inorder.index(root.val)
            root.right = helper(inorder[div + 1 :], postorder)  # [7]
            root.left = helper(inorder[:div], postorder)
            return root

        return helper(inorder, postorder)


# Solution2: Recusion
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
        # [3(tail of right), 9(head of left), 20(right child of 3), ]
        #
        mapper = {}
        for index, val in enumerate(inorder):
            mapper[val] = index

        def helper(low, high):
            if low > high:
                return None
            root = TreeNode(postorder.pop())
            div = mapper[root.val]
            root.right = helper(div + 1, high)  # [7]
            root.left = helper(low, div - 1)
            return root

        return helper(0, len(inorder) - 1)  # O(n), O(n)
