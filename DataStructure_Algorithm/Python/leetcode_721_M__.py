# 721. Accounts Merge
from collections import defaultdict

# Solution1:
    # create a graph where each row given one index and the index will be the key of graph
    # dfs traversing accounts



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        visited = [False for _ in range(len(accounts))]
        graph = defaultdict(list)
        res = []
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                graph[email].append(i)

        def dfs(i, emails):
            if visited[i]:
                return None
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in graph[email]:
                    dfs(neighbor, emails)

        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
