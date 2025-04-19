# 2300. Successful Pairs of Spells and Potions

from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            result.append(n - left)
        return result


import bisect


class Solution2:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        n = len(potions)
        res = []

        for spell in spells:
            target = (success + spell - 1) // spell
            idx = bisect.bisect_left(potions, target)
            res.append(n - idx)
        return res
