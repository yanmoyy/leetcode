# 399. Evaluate Division

from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        adj = defaultdict(list)
        visited = defaultdict(bool)
        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
            visited[a] = False
            visited[b] = False

        def dfs(node, target):
            if node not in adj or target not in adj:
                return -1.0

            if node == target:
                return 1.0

            visited[node] = True
            for next, value in adj[node]:
                if not visited[next]:
                    res = dfs(next, target)
                    if res != -1.0:
                        return res * value
            return -1.0

        res = []
        for a, b in queries:
            for key in visited:
                visited[key] = False
            res.append(dfs(a, b))
        return res
