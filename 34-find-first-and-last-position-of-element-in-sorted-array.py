from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        r = bisect_right(nums, target)
        # if not nums:
        #     return [-1, -1]
        # if l >= len(nums) or nums[l] != target:
        #     l = -1
        # r -= 1
        # if nums[r] != target:
        #     r = -1
        # return [l, r]
        if l == r:
            return [-1, -1]
        return [l, r-1]
