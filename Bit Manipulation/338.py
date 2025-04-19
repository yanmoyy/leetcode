# 338. Counting Bits

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i & (i - 1)] + 1

        return dp


class Solution2:
    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n + 1)

        for i in range(1, n + 1):
            arr[i] = arr[i >> 1] + (i % 2)

        return arr
