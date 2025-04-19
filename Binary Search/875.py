# 875. Koko Eating Bananas

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if self.canEatAll(piles, mid, h):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def canEatAll(self, piles: List[int], speed: int, h: int) -> bool:
        time = 0
        for pile in piles:
            rem = pile % speed
            time += pile // speed
            if rem > 0:
                time += 1
        return time <= h
