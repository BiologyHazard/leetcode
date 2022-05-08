from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0
        pos = 0
        while len(arr) > 1:
            Min = 0x7fffffff
            for i in range(len(arr) - 1):
                if Min > arr[i] * arr[i+1]:
                    Min = arr[i] * arr[i+1]
                    pos = i if arr[i] < arr[i+1] else i+1
            ans += Min
            del arr[pos]
        return ans
