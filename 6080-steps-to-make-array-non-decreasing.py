from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        l = [0 for _ in range(n)]
        stack = []
        ans = 0
        for i in range(n):
            prev = 0
            while stack and nums[i] >= nums[stack[-1]]:
                prev = max(prev, l[stack.pop()])
            stack.append(i)
            if len(stack) > 1:
                l[i] = prev + 1
            else:
                l[i] = 0
            ans = max(ans, l[i])
        return ans
