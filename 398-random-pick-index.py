from typing import List
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.bucket = {}
        # for i, num in enumerate(nums):
        #     if num in self.bucket:
        #         self.bucket[num].append(i)
        #     else:
        #         self.bucket[num] = [i]
        self.nums = nums

    def pick(self, target: int) -> int:
        # return random.choice([i for i, num in enumerate(self.nums) if num == target])
        if target in self.bucket:
            pass
        else:
            self.bucket[target] = []
            for i, num in enumerate(self.nums):
                if num == target:
                    self.bucket[target].append(i)
        return random.choice(self.bucket[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
