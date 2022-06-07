import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            x = self.x + self.r * (2 * random.random() - 1)
            y = self.y + self.r * (2 * random.random() - 1)
            if (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2:
                return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
