# 2352. Equal Row and Column Pairs

from typing import List
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = defaultdict(int)
        for row in grid:
            count[tuple(row)] += 1
        res = 0
        for col in zip(*grid):
            res += count[col]
        return res
