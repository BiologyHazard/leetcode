class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        TIMES = [None, None, 3, 3, 3, 3, 3, 4, 3, 4]
        MOD = 10**9 + 7

        pks = list(map(int, pressedKeys))
        n = len(pks)
        dp = [0 for i in range(n+1)]
        dp[0] = 1

        for i in range(n):
            time = TIMES[pks[i]]
            for j in range(i-1, i-time-1, -1):
                if j < -1:
                    break
                if pks[j] != pks[i]:
                    dp[i+1] += dp[j+1]
                    dp[i+1] %= MOD
                    break
                dp[i+1] += dp[j+1]
                dp[i+1] %= MOD

        return dp[n]
