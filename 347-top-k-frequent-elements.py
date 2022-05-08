from collections import Counter
from heapq import nlargest
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = list(Counter(nums).items())
        return nlargest(k, c, lambda x: x[1])
