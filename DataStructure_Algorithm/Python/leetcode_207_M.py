# 207. Course Schedule
# Solution1.1 : dfs + backtrack
# create a graph for dependencies
# search through the graph dependencies by dependencies (dfs)
#   if we reach a node that has already visisted, then we know it has a cycle -> return False
# if all visited and nothig wrong -> return True
# at the same time, we need to record the cycle
# we need a array to record visisted
# two ways to record the visited, one is the current visited to identify cycle
# the other one is to prevent revisited the nodes already visited (do this after)
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
        return True  # O(V+E), O(V+E)


# Solution1.2 : sma e as 1.1 but more intuitive
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        for curr, prev in prerequisites:
            graph[prev].append(curr)

        for i in range(numCourses):
            if self.cycle(graph, visited, i):
                return False
        return True

    def cycle(self, graph, visited, i):
        # we set -1 to curr visited and 1 to already visited in past
        if visited[i] == -1:
            return True
        if visited[i] == 1:
            return False
        visited[i] = -1
        for j in graph[i]:
            if self.cycle(graph, visited, j):
                return True
        visited[i] = 1
        return False
