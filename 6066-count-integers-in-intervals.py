from operator import itemgetter
from bisect import bisect_right


class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.c = 0

    def add(self, left: int, right: int) -> None:
        right += 1
        l = bisect_right(self.intervals, left, key=itemgetter(0))
        r = bisect_right(self.intervals, right, key=itemgetter(1))

        if l > 0 and left <= self.intervals[l-1][1]:
            left = self.intervals[l-1][0]
            l -= 1
        if r < len(self.intervals) and right >= self.intervals[r][0]:
            right = self.intervals[r][1]
            r += 1

        for i in range(l, r):
            self.c -= self.intervals[i][1] - self.intervals[i][0]
        self.c += right - left

        del self.intervals[l:r]
        self.intervals.insert(l, (left, right))

    def count(self) -> int:
        return self.c


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
