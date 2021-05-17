# 105. Construct Binary Tree from Preorder and Inorder Traversal


# Solution: recursive, we can see that the inorder is the key to for the structure and postorder/preorder is the node for
# building the tree. Becareful that the order of the recursion matters due to the order of the preorder/postorder tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorderIter = iter(preorder)
        mapper = {}
        for key, val in enumerate(inorder):
            mapper[val] = key

        def helper(low, high):
            if low > high:
                return None
            root_val = next(preorderIter)  # 1, 2, 3
            root = TreeNode(root_val)  # 1
            rootIndex = mapper[root_val]  # 1, 0, 2
            root.left = helper(low, rootIndex - 1)  # 1.left = 2
            root.right = helper(rootIndex + 1, high)  # 1.right = 3
            return root 

        return helper(0, len(inorder) - 1)
