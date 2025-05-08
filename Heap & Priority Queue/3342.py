from heapq import heappop, heappush
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heap = [(0, 0, 0, 1)]  # (current time, row, col, next cost)
        min_time = [[float("inf")] * m for _ in range(n)]
        min_time[0][0] = 0

        while heap:
            cur_t, x, y, c = heappop(heap)
            if (x, y) == (n - 1, m - 1):
                return cur_t
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                nxt_t = max(cur_t, moveTime[nx][ny]) + c
                nxt_c = 2 if c == 1 else 1
                if nxt_t < min_time[nx][ny]:
                    min_time[nx][ny] = nxt_t
                    heappush(heap, (nxt_t, nx, ny, nxt_c))
        return -1
