from typing import List
from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            if Counter(words[i-1]) == Counter(words[i]):
                del words[i]
            else:
                i += 1
        return words
