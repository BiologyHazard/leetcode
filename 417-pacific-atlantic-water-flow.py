from typing import List, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def empty_list(m, n, x):
            return [[x for _ in range(n)] for _ in range(m)]

        def bfs(start: List[Tuple[int, int]]):
            q = start
            visited = empty_list(m, n, False)
            for x, y in q:
                visited[x][y] = True

            while q:
                x, y = q.pop(0)
                visited[x][y] = True
                for dx, dy in DIRECTIONS:
                    x_p = x + dx
                    y_p = y + dy
                    if (0 <= x_p < m) and (0 <= y_p < n) and (not visited[x_p][y_p]):
                        if heights[x_p][y_p] >= heights[x][y]:
                            q.append((x_p, y_p))
                            visited[x_p][y_p] = True
            return visited

        m = len(heights)
        n = len(heights[0])

        pacific_q = []
        pacific_q.extend([(0, i) for i in range(n)])
        pacific_q.extend([(i, 0) for i in range(1, m)])
        pacific_visited = bfs(pacific_q)

        atlantic_q = []
        atlantic_q.extend([(m-1, i) for i in range(n)])
        atlantic_q.extend([(i, n-1) for i in range(m-1)])
        atlantic_visited = bfs(atlantic_q)

        ans = []
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    ans.append((i, j))
        return ans


if __name__ == '__main__':
    print(Solution().pacificAtlantic([[2, 1], [1, 2]]))
