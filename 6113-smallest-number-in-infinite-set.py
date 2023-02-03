class SmallestInfiniteSet:

    def __init__(self):
        self.s = set(range(1, 1002))

    def popSmallest(self) -> int:
        m = min(self.s)
        self.s.remove(m)
        return m

    def addBack(self, num: int) -> None:
        self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
