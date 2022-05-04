from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # def p(l, r):
        #     if not r:
        #         ans.append(l)
        #         return
        #     for i, x in enumerate(r):
        #         p(l + [x], r[:i] + r[i+1:])
        # p([], nums)
        for x in permutations(nums):
            ans.append(list(x))
        return ans
