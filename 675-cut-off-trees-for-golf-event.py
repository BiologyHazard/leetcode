from collections import deque
from itertools import pairwise
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(x1, y1, x2, y2):
            q = deque()
            dis = [[-1 for j in range(n)] for i in range(m)]
            q.append((x1, y1))
            dis[x1][y1] = 0
            while q:
                x, y = q.popleft()
                cur = dis[x][y]
                if (x, y) == (x2, y2):
                    return cur
                for dx, dy in DIRECTIONS:
                    xx, yy = x+dx, y+dy
                    if 0 <= xx < m and 0 <= yy < n:
                        if forest[xx][yy] > 0 and dis[xx][yy] == -1:
                            q.append((xx, yy))
                            dis[xx][yy] = cur + 1

            return -1

        m, n = len(forest), len(forest[0])
        l = sorted([(i, j) for i in range(m) for j in range(
            n) if forest[i][j] > 1], key=lambda x: forest[x[0]][x[1]])
        ans = 0
        for (x1, y1), (x2, y2) in pairwise([(0, 0)] + l):
            d = bfs(x1, y1, x2, y2)
            if d == -1:
                return -1
            ans += d
        return ans
