from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        l = 0
        r = len(nums) - 1
        while True:
            s = nums_sorted[l] + nums_sorted[r]
            if s == target:
                break
            elif s < target:
                l += 1
            else:
                r -= 1
        ans = []
        for i, x in enumerate(nums):
            if x == nums_sorted[l] or x == nums_sorted[r]:
                ans.append(i)
        return ans
