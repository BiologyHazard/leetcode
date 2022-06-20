from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        dx1, dy1 = x2-x1, y2-y1
        dx2, dy2 = x3-x1, y3-y1
        if dx1*dy2 == dy1*dx2:
            return False
        return True
