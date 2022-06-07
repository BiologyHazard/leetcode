import imp
from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = [-1 for _ in range(10**6 + 1)]
        for i, num in enumerate(nums):
            d[num] = i
        for op0, op1 in operations:
            nums[d[op0]] = op1
            d[op1] = d[op0]
            d[op0] = -1
        return nums
