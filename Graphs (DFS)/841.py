# 841. Keys and Rooms

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        self.cnt = 0

        def dfs(node: int):
            visited[node] = True
            self.cnt += 1
            for next in rooms[node]:
                if not visited[next]:
                    dfs(next)

        dfs(0)
        return self.cnt == n
