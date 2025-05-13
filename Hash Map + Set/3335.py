from typing import Counter


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        n = t // 26
        r = t % 26
        dp = [[0] * 26 for _ in range(n + 1)]
        count = Counter(s)
        for i in range(26):
            dp[0][i] = count[chr(ord("a") + i)]

        for i in range(1, n + 1):
            for j in range(26):
                if j == 1:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][25] % mod
                else:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod
        total = 0
        for i in range(26):
            total = (total + dp[n][i]) % mod
            if i >= 26 - r:
                total = (total + dp[n][i]) % mod
        return total


class Solution2(object):
    # Per Each char
    def lengthAfterTransformations(self, s, t):
        mod = 10**9 + 7
        dp = [0] * (t + 26)
        for i in range(26):
            dp[i] = 1
        for i in range(26, t + 26):
            dp[i] = (dp[i - 26] + dp[i - 25]) % mod
        ans = 0
        for ch in s:
            ans = (ans + dp[ord(ch) - ord("a") + t]) % mod
        return ans
