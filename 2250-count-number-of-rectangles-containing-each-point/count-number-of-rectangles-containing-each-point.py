from typing import List
from bisect import bisect_left


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # rectangles.sort(key=lambda x: x[1])
        # print(rectangles)
        # rec_index = [len(rectangles) for _ in range(101)]
        # pre_h = -1
        # for i, (l, h) in enumerate(rectangles):
        #     if h > pre_h:
        #         for j in range(pre_h+1, h+1):
        #             rec_index[j] = i
        #         pre_h = h
        # print(rec_index)
        # ans = [0 for point in points]
        # for i, (x, y) in enumerate(points):
        #     for l, h in rectangles[rec_index[y]:]:
        #         if x <= l:
        #             ans[i] += 1
        # return ans
        rect_h = [[] for _ in range(101)]

        for l, h in rectangles:
            rect_h[h].append(l)

        for h in range(101):
            rect_h[h].sort()

        ans = []
        for x, y in points:
            count = 0
            for h in range(y, 101):
                idx = bisect_left(rect_h[h], x)
                count += len(rect_h[h]) - idx
            ans.append(count)
        return ans


print(Solution().countRectangles([[6, 4], [10, 2], [5, 5], [1, 6], [3, 2], [9, 5], [7, 6]],
                                 [[2, 1], [2, 8], [8, 4], [10, 8], [5, 6], [1, 4], [2, 4], [2, 2], [6, 10]]))
