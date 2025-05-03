from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        numbers_cnt = defaultdict(int)
        n = len(tops)
        for i in tops:
            numbers_cnt[i] += 1
        for i in bottoms:
            numbers_cnt[i] += 1
        target = max(numbers_cnt, key=lambda k: numbers_cnt[k])
        top_cnt, bot_cnt, chk_cnt = 0, 0, 0
        for i in range(n):
            is_top = tops[i] == target
            is_bot = bottoms[i] == target
            chk_cnt += is_top or is_bot
            top_cnt += is_top
            bot_cnt += is_bot
        if chk_cnt == n:
            return min(n - top_cnt, n - bot_cnt)
        else:
            return -1
