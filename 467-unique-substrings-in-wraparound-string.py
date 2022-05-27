from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        prechar = None
        for char in p:
            if prechar is not None and (ord(char) - ord(prechar)) % 26 == 1:
                k += 1
            else:
                k = 1
            dp[char] = max(dp[char], k)
            prechar = char
        return sum(dp.values())
