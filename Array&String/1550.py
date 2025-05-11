from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_cnt = 0
        for i in arr:
            if i % 2 == 1:
                odd_cnt += 1
            else:
                odd_cnt = 0
            if odd_cnt >= 3:
                return True
        return False
