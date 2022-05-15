from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        s = [0 for _ in range(30)]
        for candidate in candidates:
            b = f'{candidate:b}'
            for j, p in enumerate(reversed(b)):
                s[j] += int(p)
        return max(s)
