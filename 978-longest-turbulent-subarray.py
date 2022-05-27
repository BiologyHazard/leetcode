from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dp = 1
        cmp = 0
        ans = 1
        for i in range(1, n):
            if cmp == 1 and arr[i-1] < arr[i]:
                dp += 1
                cmp = -1
            elif cmp == -1 and arr[i-1] > arr[i]:
                dp += 1
                cmp = 1
            else:
                if arr[i-1] < arr[i]:
                    dp = 2
                    cmp = -1
                elif arr[i-1] > arr[i]:
                    dp = 2
                    cmp = 1
                else:
                    dp = 1
                    cmp = 0
            ans = max(ans, dp)
        return ans
