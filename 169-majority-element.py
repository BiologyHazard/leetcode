from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        value = None
        for num in nums:
            if num == value:
                count += 1
            else:
                count -= 1
            if count < 0:
                value = num
                count = 1
        return value
