from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        s1 = 0
        s2 = sum(nums)
        n = len(nums)
        avg = []
        for i in range(n):
            s1 += nums[i]
            s2 -= nums[i]
            if i == n-1:
                avg.append(abs(s1 // (i+1)))
            else:
                avg.append(abs(s1 // (i+1) - s2 // (n-i-1)))
        return min(enumerate(avg), key=lambda x: x[1])[0]
