# 714. Best Time to Buy and Sell Stock with Transaction Fee

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(n)]

        dp[0][0] = 0  # max profit at day 0 with 0 stock
        dp[0][1] = -prices[0]  # max profit at day 0 with 1 stock

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]
