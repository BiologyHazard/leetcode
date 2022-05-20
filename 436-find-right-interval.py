from typing import List
from operator import itemgetter
from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        pcd = sorted(enumerate(intervals), key=itemgetter(1))
        ans = []
        for start, end in intervals:
            pos = bisect_left(pcd, end, key=lambda x: x[1][0])
            if pos == n:
                pos = -1
            else:
                pos = pcd[pos][0]
            ans.append(pos)
        return ans
