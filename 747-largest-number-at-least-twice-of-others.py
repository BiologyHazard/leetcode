from typing import *


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        i = nums.index(m)
        if all(map(lambda x: m >= 2*x, nums[:i] + nums[i+1:])):
            return i
        return -1
