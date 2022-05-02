from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp1 = [nums[0]]
        # dp2 = [0]
        # for num in nums[1:]:
        #     dp1.append(num + dp2[-1])
        #     dp2.append(max(dp1[-2], dp2[-1]))
        # return max(dp1[-1], dp2[-1])
        dp = [nums[0]]
        if len(nums) > 1:
            dp.append(max(nums[0], nums[1]))
        for num in nums[2:]:
            dp.append(max(dp[-1], dp[-2] + num))
        return dp[-1]
