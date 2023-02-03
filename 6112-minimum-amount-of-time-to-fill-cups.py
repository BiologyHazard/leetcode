from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        count = 0
        while any(i > 0 for i in amount):
            count += 1
            idx = amount.index(min(amount))
            for i in range(3):
                if i != idx:
                    amount[i] -= 1
        return count
