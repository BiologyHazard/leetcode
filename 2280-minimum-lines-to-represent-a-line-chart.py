from decimal import Decimal
from operator import itemgetter
from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        stockPrices.sort(key=itemgetter(0))
        prev_k = None
        ans = 0
        for i in range(n-1):
            x1, y1 = stockPrices[i]
            x2, y2 = stockPrices[i+1]
            k = Decimal(y1 - y2) / Decimal(x1 - x2)
            if prev_k is None or not k == prev_k:
                ans += 1
            prev_k = k
        return ans
