from collections import Counter


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = Counter(s)
        return int(c[letter] / len(s) * 100)
