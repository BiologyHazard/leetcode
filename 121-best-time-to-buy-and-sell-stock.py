from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Knowing which date has the lowest price before a given day i
        low = prices[0]  # Contains the lowest price from day0 to dayi
        ans = 0
        for i, price in enumerate(prices[1:]):
            # When calculating the profit, use min( day0 ~ i-1 ) !!  Starts with max(0, p1-p0)
            ans = max(ans, price - low)
            low = min(low, price)  # Then renew the lowest price
        return ans
