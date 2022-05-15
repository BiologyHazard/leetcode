from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        max_ = special[0] - bottom
        for i in range(len(special) - 1):
            max_ = max(max_, special[i+1] - special[i] - 1)
        max_ = max(max_, top - special[-1])
        return max_
