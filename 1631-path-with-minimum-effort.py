from typing import List
# from collections import deque


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(heights), len(heights[0])
        visited = [[False for j in range(n)] for i in range(m)]
        # visited[0][0] = True
        effort = [[0x7fffffff for j in range(n)] for i in range(m)]
        effort[0][0] = 0
        for i in range(m*n):
            min_x = min_y = 0
            min_eff = 0x7fffffff
            for j in range(m):
                for k in range(n):
                    if (not visited[j][k]) and (effort[j][k] < min_eff):
                        min_x, min_y = j, k
                        min_eff = effort[j][k]
            x, y = min_x, min_y
            visited[x][y] = True
            for dx, dy in DIRECTIONS:
                xx, yy = x+dx, y+dy
                if (0 <= xx < m) and (0 <= yy < n):
                    effort[xx][yy] = min(
                        effort[xx][yy],
                        max(effort[x][y], abs(heights[x][y] - heights[xx][yy])))
        return effort[-1][-1]


if __name__ == '__main__':
    print(Solution().minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [
          1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
