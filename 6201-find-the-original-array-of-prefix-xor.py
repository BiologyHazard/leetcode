from typing import List
from itertools import pairwise


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return list(map((lambda x: x[0] ^ x[1]), pairwise([0] + pref)))
