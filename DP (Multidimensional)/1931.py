class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        # 1: Generate valid column colorings
        def generate_states(pos, current, states):
            if pos == m:
                states.append(current[:])
                return
            for color in range(3):
                if pos > 0 and current[-1] == color:
                    continue
                current.append(color)
                generate_states(pos + 1, current, states)
                current.pop()

        valid_states = []
        generate_states(0, [], valid_states)
        state_count = len(valid_states)

        # 2: Compute compatible state pairs
        compatible = [[False] * state_count for _ in range(state_count)]
        for i in range(state_count):
            for j in range(state_count):
                compatible[i][j] = all(
                    valid_states[i][k] != valid_states[j][k] for k in range(m)
                )

        # 3: Dynamic Programming
        dp = [[0] * state_count for _ in range(n + 1)]
        # dp[i][j] count all ways if current column state is j
        dp[0][0] = 1  # Base case : one way for empty grid

        for s in range(state_count):
            dp[1][s] = dp[0][0]

        for j in range(2, n + 1):
            for s in range(state_count):
                for t in range(state_count):
                    if compatible[t][s]:
                        dp[j][s] = (dp[j][s] + dp[j - 1][t]) % MOD

        result = sum(dp[n][s] for s in range(state_count)) % MOD
        return result
