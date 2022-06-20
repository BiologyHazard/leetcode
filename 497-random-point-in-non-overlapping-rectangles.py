import imp
import random
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.n = len(rects)
        self.weights = []
        for a, b, x, y in rects:
            s = (x-a+1)*(y-b+1)
            self.weights.append(s)
        # print(self.weights)
        # print(self.rects)

    def pick(self) -> List[int]:
        c = random.choices(range(self.n), self.weights)[0]
        a, b, x, y = self.rects[c]
        return [random.randint(a, x), random.randint(b, y)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
