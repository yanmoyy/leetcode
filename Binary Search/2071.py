from collections import deque
from typing import List


class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def can_assign(mid):
            dq = deque()
            w = len(workers) - 1
            p = pills

            for t in reversed(tasks[:mid]):
                if dq and dq[0] >= t:
                    dq.popleft()
                elif w >= 0 and workers[w] >= t:
                    w -= 1
                else:
                    while w >= 0 and workers[w] + strength >= t:
                        dq.append(workers[w])
                        w -= 1
                    if not dq or p == 0:
                        return False
                    dq.pop()
                    p -= 1
            return True

        left, right = 0, min(n, m)

        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                left = mid + 1
            else:
                right = mid - 1

        return left - 1
