from bisect import bisect_left
from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def solve(k: int) -> bool:
            return sum(ceil(i / k) for i in piles) <= h
        return bisect_left(range(1, 10**9), True, key=solve) + 1
