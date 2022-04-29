from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        a = [max(i) for i in grid]
        b = [max(i) for i in zip(*grid)]
        return sum(sum(min(a[i], b[j]) - grid[i][j] for j in range(len(grid[0]))) for i in range(len(grid)))
