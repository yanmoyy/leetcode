# 1466. Reorder Routes to Make All Paths Lead to the City Zero

from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        self.cnt = 0

        for u, v in connections:
            adj[u].append((v, True))
            adj[v].append((u, False))

        def dfs(node):
            visited[node] = True
            for next, is_forward in adj[node]:
                if not visited[next]:
                    if is_forward:
                        self.cnt += 1
                    dfs(next)

        dfs(0)
        return self.cnt
