from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(line) != sorted(line) for line in zip(*strs))
