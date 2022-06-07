from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        j = 0
        ans = 0
        while i < n:
            cur = nums[i]
            while j < n and cur + k >= nums[j]:
                j += 1
            i = j
            ans += 1
        return ans
