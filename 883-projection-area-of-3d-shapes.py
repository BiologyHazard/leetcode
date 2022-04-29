from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in grid:
            for j in i:
                if j > 0:
                    ans += 1
            ans += max(i)
        for i in zip(*grid):
            ans += max(i)
        return ans
