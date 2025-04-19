# 790. Domino and Tromino Tiling


class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7

        dp = [[0] * 3 for _ in range(n + 1)]
        dp[0][0] = 1
        dp[1][0] = 1

        for i in range(2, n + 1):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][0] + dp[i - 2][0]) % mod
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][2]) % mod
            dp[i][2] = (dp[i - 2][0] + dp[i - 1][1]) % mod

        return dp[n][0]
        """
        dp[x][y] = x is the number of columns
        y = 0 : the way to fill all the rows
        y = 1 : ... only 1st row
        y = 2 : ... only 2nd row
        dp: the way to cover the remaining part

        dp[0][0] = 1 : one way to not cover any row

        dp[1][0] = 1 : there is only one way to cover the remaining part ( | )
        dp[1][1] = 0 : there is no way if only 1st row is covered
        dp[1][2] = 0 : there is no way if only 2nd row is covered

        dp[2][0] = dp[1][1] + dp[1][2] + dp[1][0] + dp[0][0] = 2
        dp[2][1] = dp[0][0] + dp[1][2] = 1
        dp[2][2] = dp[0][0] + dp[1][1] = 1

        dp[3][0] = dp[2][1] + dp[2][2] + dp[2][0] + dp[1][0] = 5
        dp[3][1] = dp[1][0] + dp[2][2] 
        dp[3][2] = dp[1][0] + dp[2][1]

        """
