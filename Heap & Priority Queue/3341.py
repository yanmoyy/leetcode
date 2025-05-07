import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        time = [[-1] * m for _ in range(n)]
        minh = []
        heapq.heappush(minh, (0, (0, 0)))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while minh:
            cur_t, (x, y) = heapq.heappop(minh)
            if time[x][y] != -1 and cur_t >= time[x][y]:
                continue
            time[x][y] = cur_t
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and time[nx][ny] == -1:
                    next_t = max(moveTime[nx][ny], cur_t) + 1
                    heapq.heappush(minh, (next_t, (nx, ny)))
        return time[n - 1][m - 1]
