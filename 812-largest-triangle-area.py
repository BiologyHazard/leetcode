from typing import List
from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a: List[int], b: List[int], c: List[int]) -> float:
            x1 = b[0] - a[0]
            x2 = c[0] - a[0]
            y1 = b[1] - a[1]
            y2 = c[1] - a[1]
            return abs(x1*y2 - x2*y1) / 2

        max_ = 0.0
        for a, b, c in combinations(points, 3):
            max_ = max(max_, area(a, b, c))
        return max_
