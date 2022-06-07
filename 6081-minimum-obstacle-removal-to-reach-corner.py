from typing import List
from collections import deque


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        q = deque()
        dis = [[-1 for _ in range(n)] for _ in range(m)]
        q.append((0, 0))
        dis[0][0] = 0
        while q:
            x, y = q.popleft()
            # print(x, y, dis[x][y])
            for dx, dy in DIRECTIONS:
                xx, yy = x+dx, y+dy
                if 0 <= xx < m and 0 <= yy < n:
                    if dis[xx][yy] == -1:
                        if grid[xx][yy] == 0:
                            q.appendleft((xx, yy))
                            dis[xx][yy] = dis[x][y]
                        else:
                            q.append((xx, yy))
                            dis[xx][yy] = dis[x][y] + 1
        return dis[-1][-1]
