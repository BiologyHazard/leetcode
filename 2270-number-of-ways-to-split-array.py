from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sl = 0
        sr = sum(nums)
        ans = 0
        n = len(nums)
        for i in range(n-1):
            sl += nums[i]
            sr -= nums[i]
            if sl >= sr:
                ans += 1
        return ans
