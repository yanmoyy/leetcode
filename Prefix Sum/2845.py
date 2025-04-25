from collections import defaultdict
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        freq = defaultdict(int)
        cnt, ans = 0, 0
        freq[0] = 1
        for i in nums:
            if i % modulo == k:
                cnt += 1
            rem = cnt % modulo
            target = (rem - k + modulo) % modulo
            ans += freq[target]
            freq[target] += 1
        return ans
