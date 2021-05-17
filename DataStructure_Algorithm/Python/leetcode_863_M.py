#863. All Nodes Distance K in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # turn it into a graph like tree, means create another pointer called parent 
        # for each node
        # use bfs, start from the target node
        def dfs(root, parent):
            if not root: return root
            root.parent = parent
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)
        result = [target]
        visited = {target}
        for _ in range(k):
            nextNodes = []
            for cur in result:
                for node in [cur.left, cur.right, cur.parent]:
                    if node not in visited and node:
                        visited.add(node)
                        nextNodes.append(node)
            result = nextNodes
        return [node.val for node in result]