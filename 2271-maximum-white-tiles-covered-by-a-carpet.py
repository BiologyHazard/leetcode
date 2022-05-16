from typing import List
from operator import itemgetter


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=itemgetter(0))
        n = len(tiles)
        count = 0
        j = 0
        ans = 0
        for i in range(n):
            start = tiles[i][0]
            end = start + carpetLen - 1
            if i > 0:
                count -= tiles[i-1][1] - tiles[i-1][0] + 1
            while j < n and tiles[j][1] <= end:
                count += tiles[j][1] - tiles[j][0] + 1
                j += 1
            if j < n and tiles[j][0] <= end:
                ans = max(ans, count + end - tiles[j][0] + 1)
            else:
                ans = max(ans, count)
        return ans
