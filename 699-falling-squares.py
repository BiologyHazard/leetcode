from bisect import bisect_right
from operator import itemgetter
from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        heights = [(0, 0)]
        ans = []
        max_height = 0

        for pos, side_length in positions:
            l = bisect_right(heights, pos, key=itemgetter(0))
            r = bisect_right(heights, pos + side_length, key=itemgetter(0))

            if r < len(heights) and heights[r-1][0] == pos + side_length:
                right = heights[r-2][1]
                height = max(heights[x][1] for x in range(l-1, r-1))
            else:
                right = heights[r-1][1]
                height = max(heights[x][1] for x in range(l-1, r))

            del heights[l:r]
            heights.insert(l, (pos, height + side_length))
            heights.insert(l+1, (pos + side_length, right))

            max_height = max(max_height, height + side_length)
            ans.append(max_height)

        return ans
