# 210. Course Schedule II

# Solution1: same as #207, just add a array to store the answer
from collections import defaultdict


class Solution:
    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        # create the graph
        # visited = [0], 1, -1
        # if not prerequisites: return []
        graph = defaultdict(list)  # [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        path = []
        for curr, prev in prerequisites:
            graph[curr].append(prev)

        for i in range(numCourses):
            if not self.findSol(graph, visited, i, path):
                return []
        return path

    def findSol(self, graph, visited, i, path):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for j in graph[i]:
            if not self.findSol(graph, visited, j, path):
                return False

        visited[i] = 1
        path.append(i)
        return True  # O(V+E), O(V+E)
