from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = [0]*101
        for i in nums:
            a[i] += 1
        for i in range(1, 101):
            a[i] += a[i-1]
        return [a[i-1] if i > 0 else 0 for i in nums]
