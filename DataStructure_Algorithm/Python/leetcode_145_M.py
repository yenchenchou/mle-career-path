# 94. Binary Tree Postorder Traversal -> refer to 144, 94 

# Solution1: Recursion
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if not root: return []
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.val)
    # O(n), O(n) if very unbalanced tree, avg is O(logn)