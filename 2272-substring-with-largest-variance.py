# 该解法未通过，TLE

from collections import defaultdict


class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        ans = 0
        for start in range(n):
            c = defaultdict(int)
            for end in range(start, n):
                c[s[end]] += 1
                if max(c.values()) - min(c.values()) > ans:
                    ans = max(c.values()) - min(c.values())
        return ans
