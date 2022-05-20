from typing import List
from itertools import pairwise


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {k: v for v, k in enumerate(order)}
        return all(s <= t for s, t in pairwise([dictionary[c] for c in word] for word in words))
