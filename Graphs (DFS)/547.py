# 547. Number of Provinces

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        self.cnt = 0

        def dfs(node):
            visited[node] = True
            for i in range(n):
                if isConnected[node][i] and not visited[i]:
                    dfs(i)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                self.cnt += 1

        return self.cnt
