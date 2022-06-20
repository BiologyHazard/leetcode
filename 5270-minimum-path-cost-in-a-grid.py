from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[grid[0][i] for i in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(n):
                mincost = 1 << 20
                for k in range(n):
                    mincost = min(
                        mincost, dp[i-1][k] + moveCost[grid[i-1][k]][j] + grid[i][j])
                dp[i][j] = mincost
        # print(dp)
        return min(dp[-1])
