# 933. Number of Recent Calls

from collections import deque


class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        q = self.q
        q.append(t)
        while q[0] < t - 3000:
            q.popleft()
        return len(q)
