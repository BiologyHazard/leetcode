from math import log2


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n <= 0 else log2(n) - int(log2(n)) < 1e-10
