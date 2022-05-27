from typing import List
from bisect import bisect_left


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        ans = len(words)
        l1 = []
        l2 = []
        for i, word in enumerate(words):
            if word == word1:
                l1.append(i)
            elif word == word2:
                l2.append(i)
        # print(l1, l2)
        for pos in l1:
            l = bisect_left(l2, pos)
            nearest = len(words)
            if l < len(l2):
                nearest = min(nearest, l2[l] - pos)
            if l > 0:
                nearest = min(nearest, pos - l2[l-1])
            ans = min(ans, nearest)
        return ans
