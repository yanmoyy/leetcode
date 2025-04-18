# 994. Rotting Oranges

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROTTEN = 2
        FRESH = 1
        max_dist = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == ROTTEN:
                    q.append((i, j, 0))

        while q:
            x, y, dist = q.popleft()
            max_dist = max(max_dist, dist)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if grid[nx][ny] == FRESH:
                    grid[nx][ny] = ROTTEN
                    q.append((nx, ny, dist + 1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == FRESH:
                    return -1

        return max_dist
