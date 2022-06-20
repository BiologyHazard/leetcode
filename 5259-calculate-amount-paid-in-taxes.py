from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        prev_upper = 0
        for upper, percent in brackets:
            if income < prev_upper:
                break
            if income < upper:
                ans += (income - prev_upper) * percent
            else:
                ans += (upper - prev_upper) * percent
            prev_upper = upper
        return ans / 100
