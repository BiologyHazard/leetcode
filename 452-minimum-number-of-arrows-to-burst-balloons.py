from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        l, r = points[0]
        ans = 1
        for start, end in points:
            if start <= r and end >= l:
                l = max(l, start)
                r = min(r, end)
            else:
                ans += 1
                l, r = start, end
        return ans
