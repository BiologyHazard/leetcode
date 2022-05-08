from typing import List
from functools import lru_cache


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(x: int, y: int, snum: int) -> bool:
            if not (0 <= x < m and 0 <= y < n):
                return False

            if grid[x][y] == '(':
                snum += 1
            else:
                snum -= 1

            if (x, y) == (m-1, n-1):
                if snum == 0:
                    return True
                return False

            if snum < 0:
                return False

            return dfs(x+1, y, snum) or dfs(x, y+1, snum)

        m, n = len(grid), len(grid[0])
        return dfs(0, 0, 0)
