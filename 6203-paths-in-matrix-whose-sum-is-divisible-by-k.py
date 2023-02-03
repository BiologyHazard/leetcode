from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        paths = [[[0 for _ in range(k)] for _ in range(n+1)]
                 for _ in range(m+1)]
        paths[1][1][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for s in range(k):
                    paths[i+1][j+1][s] += paths[i][j+1][(
                        s - grid[i][j] + 100*k) % k] + paths[i+1][j][(s - grid[i][j] + 100*k) % k]
                    paths[i+1][j+1][s] %= MOD
                    # print(paths)
        return paths[-1][-1][0]
