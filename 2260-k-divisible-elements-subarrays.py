from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        s = set()
        for start in range(n):
            for end in range(start+1, n+1):
                sublist = nums[start:end]
                if len(list(filter(lambda x: x % p == 0, sublist))) <= k:
                    s.add(tuple(sublist))
                else:
                    break
        return len(s)
