from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        j = 0
        p = 1
        for i in range(n):
            if j < i:
                j = i
                p = 1
            while j < n and p * nums[j] < k:
                p *= nums[j]
                j += 1
            ans += j - i
            p //= nums[i]
        return ans
