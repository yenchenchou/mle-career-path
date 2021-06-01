#207. Course Schedule
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create course dependencies -> the graph
        # create visited recorder, if we visited 
        # check if the current node has been checked before
        graph = defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        for curr, prev in prerequisites:
            graph[curr].append(prev)
        
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        if visited[i] == -1:
            return False
        # record the node you visited to prevent going again once you checked there's no cycle
        if visited[i] == 1:  
            return True
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 1
        return True  #O(V+E), O(V+E)