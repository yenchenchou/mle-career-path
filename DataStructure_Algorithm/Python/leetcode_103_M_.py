# 103. Binary Tree Zigzag Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        node_queue = deque([root, None])
        flag = 1
        res = []
        level_list = deque()
        while len(node_queue) > 0:
            node = node_queue.popleft()
            if node:
                if flag == 1:
                    level_list.append(node.val)
                else:
                    level_list.appendleft(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            else:
                res.append(level_list)
                if len(node_queue) > 0:
                    node_queue.append(None)
                level_list = deque()
                flag = flag * -1
        return res

        if not root:
            return []
        queue = deque([root])
        flag = True
        res = []
        while queue:
            level_list = deque()
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if flag:
                    level_list.append(node.val)
                else:
                    level_list.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            queue.append(level_list)
            flag = not flag
        return res


# Solution1.2: my try (bfs)
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        node_queue = deque([root])
        flag = True
        res = []

        while node_queue:
            level_list = deque()
            size = len(node_queue)
            for _ in range(size):
                node = node_queue.popleft()
                if flag:
                    level_list.append(node.val)
                else:
                    level_list.appendleft(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            res.append(level_list)
            flag = not flag
        return res