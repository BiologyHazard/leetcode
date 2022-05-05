from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        UNGUARDED = 0
        GUARDED = 1
        GUARD = 2
        WALL = 3
        grid = [[UNGUARDED for j in range(n)] for i in range(m)]
        for x, y in walls:
            grid[x][y] = WALL
        for x, y in guards:
            grid[x][y] = GUARD
        for x, y in guards:
            i = x - 1
            while 0 <= i and grid[i][y] != WALL and grid[i][y] != GUARD:
                grid[i][y] = GUARDED
                i -= 1
            i = x + 1
            while i < m and grid[i][y] != WALL and grid[i][y] != GUARD:
                grid[i][y] = GUARDED
                i += 1
            i = y - 1
            while 0 <= i and grid[x][i] != WALL and grid[x][i] != GUARD:
                grid[x][i] = GUARDED
                i -= 1
            i = y + 1
            while i < n and grid[x][i] != WALL and grid[x][i] != GUARD:
                grid[x][i] = GUARDED
                i += 1
        # print(*grid, sep='\n')
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == UNGUARDED:
                    ans += 1
        return ans
