# 2336. Smallest Number in Infinite Set

import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.min_heap = []
        self.added = set()
        self.current = 1

    def popSmallest(self) -> int:
        if self.min_heap:
            res = heapq.heappop(self.min_heap)
            self.added.remove(res)
            return res
        else:
            res = self.current
            self.current += 1
            return res

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added:
            self.added.add(num)
            heapq.heappush(self.min_heap, num)
