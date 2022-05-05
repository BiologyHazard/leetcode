from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return len([word for word in words if s.startswith(word)])
