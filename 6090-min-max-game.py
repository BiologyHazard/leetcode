from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while (n := len(nums)) > 1:
            l = []
            for i in range(n // 2):
                if i % 2 == 0:
                    l.append(min(nums[2*i], nums[2*i+1]))
                else:
                    l.append(max(nums[2*i], nums[2*i+1]))
            nums = l
        return nums[0]
