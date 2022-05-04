from collections import defaultdict
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dct = defaultdict(list)
        for i, num in enumerate(cards):
            dct[num].append(i)
        ans = 0x0fffffff
        for num, l in dct.items():
            if len(l) > 1:
                for i in range(len(l) - 1):
                    ans = min(ans, l[i+1] - l[i])
        return -1 if ans == 0x0fffffff else ans + 1
