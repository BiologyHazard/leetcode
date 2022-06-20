from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        return sum(1 for i in range(len(heights)) if s[i] != heights[i])
