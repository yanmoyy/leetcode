# 1926. Nearest Exit from Entrance in Maze

from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        n, m = len(maze), len(maze[0])
        dist = [[-1 for _ in range(m)] for _ in range(n)]
        q = deque()
        q.append((entrance[0], entrance[1]))
        dist[entrance[0]][entrance[1]] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    if [x, y] != entrance:
                        return dist[x][y]
                    continue
                if maze[nx][ny] == "+" or dist[nx][ny] != -1:
                    continue
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
        return -1
