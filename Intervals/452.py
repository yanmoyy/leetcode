# 452. Minimum Number of Arrows to Burst Balloons

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res = 1
        end = points[0][1]

        for i in range(1, len(points)):
            if end < points[i][0]:
                # new balloon
                res += 1
                end = points[i][1]
        return res
