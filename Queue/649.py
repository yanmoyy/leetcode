# 649. Dota2 Senate

from typing import List
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_q, d_q = deque(), deque()
        for i, c in enumerate(senate):
            if c == "R":
                r_q.append(i)
            else:
                d_q.append(i)
        while r_q and d_q:
            if r_q[0] < d_q[0]:
                r_q.append(r_q.popleft() + n)
                d_q.popleft()
            else:
                d_q.append(d_q.popleft() + n)
                r_q.popleft()

        return "Radiant" if r_q else "Dire"
