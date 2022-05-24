from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        l = [capacity[i] - rocks[i] for i in range(n)]
        l.sort()
        ans = 0
        s = 0
        for i in l:
            if s + i <= additionalRocks:
                s += i
                ans += 1
            else:
                break
        return ans
