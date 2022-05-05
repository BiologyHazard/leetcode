from math import inf
from typing import List
from collections import deque
from bisect import bisect_right


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        def bfs(t: int) -> bool:
            rush_time = [[-1 for j in range(n)] for i in range(m)]
            q: deque[tuple[int, int]] = deque()
            q.append((0, 0))
            rush_time[0][0] = t
            while q:
                x, y = q.popleft()
                time = rush_time[x][y]
                for dx, dy in DIRECTIONS:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < m and 0 <= yy < n:
                        if (xx, yy) == (m-1, n-1):  # 如果到了安全屋
                            return spread_time[xx][yy] >= time + 1  # 只要>=就行
                        if (rush_time[xx][yy] == -1 and
                                spread_time[xx][yy] > time + 1):  # 否则要>
                            q.append((xx, yy))
                            rush_time[xx][yy] = time + 1
            return False

        m, n = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        spread_time = [[inf for j in range(n)] for i in range(m)]
        q: deque[tuple[int, int]] = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    spread_time[i][j] = 0
                    q.append((i, j))
                elif grid[i][j] == 2:
                    spread_time[i][j] = -1
        while q:
            x, y = q.popleft()
            time = spread_time[x][y]
            for dx, dy in DIRECTIONS:
                xx, yy = x + dx, y + dy
                if 0 <= xx < m and 0 <= yy < n:
                    if spread_time[xx][yy] == inf:
                        q.append((xx, yy))
                        spread_time[xx][yy] = time + 1

        if bfs(10**9):
            return 10**9

        return bisect_right(range(m*n + 1), not True,
                            key=lambda x: not bfs(x)) - 1


if __name__ == '__main__':
    print(Solution().maximumMinutes([[0, 2, 0, 0, 1], [0, 2, 0, 2, 2], [
          0, 2, 0, 0, 0], [0, 0, 2, 2, 0], [0, 0, 0, 0, 0]]))
