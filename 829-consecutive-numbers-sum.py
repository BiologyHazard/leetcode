from math import floor, sqrt


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        for i in range(1, floor(sqrt(2*n)) + 1):
            if i % 2 == 1:
                if n % i == 0 and n // i - (i+1) // 2 >= 0:
                    ans += 1
            else:
                if n % i != 0 and (2*n) % i == 0 and n // i - i // 2 >= 0:
                    ans += 1
        return ans
