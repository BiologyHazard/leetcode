from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        dp1 = [nums[0], max(nums[0], nums[1])]
        dp2 = [0, nums[1]]

        for num in nums[2:]:
            dp1.append(max(dp1[-1], dp1[-2] + num))
            dp2.append(max(dp2[-1], dp2[-2] + num))
        return max(dp1[-2], dp2[-1])
