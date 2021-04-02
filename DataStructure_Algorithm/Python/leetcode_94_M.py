# 94. Binary Tree Inorder Traversal -> refer to 144 inorder traversal

# Solution1: Recursion
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if not root: return []
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
    # O(n), O(n) if very unbalanced tree, avg is O(logn)


# Solution2: Iteration
class Solution:
    def inorderTraversal(self, root: TreeNode) -> stacList[int]:
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack: return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
    #O(n), O(n)

# Solution2.2: Iteration (My try)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif len(stack) != 0:
                node = stack.pop()
                res.append(node.val)
                root = node.right
            else:
                break
        return res  # [1, None], [1, 2, 3]->213, [1,null,3]->13, [1,2,null,3]->213, [1,null,2,3]->132
    #O(n), O(n)