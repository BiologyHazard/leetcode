class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> int:
        self.events.append((start, 1))
        self.events.append((end, -1))
        self.events.sort()
        ans = 0
        k = 0
        for i in range(len(self.events)):
            k += self.events[i][1]
            # if i == len(self.events) - 1 or self.events[i][0] < self.events[i+1][0]:
            ans = max(ans, k)
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
# from collections import defaultdict


# class MyCalendarThree:
#     def __init__(self):
#         self.tree = defaultdict(int)
#         self.lazy = defaultdict(int)

#     def update(self, start: int, end: int, l: int, r: int, idx: int):
#         if r < start or end < l:
#             return
#         if start <= l and r <= end:
#             self.tree[idx] += 1
#             self.lazy[idx] += 1
#         else:
#             mid = (l + r) // 2
#             self.update(start, end, l, mid, idx * 2)
#             self.update(start, end, mid + 1, r, idx * 2 + 1)
#             self.tree[idx] = self.lazy[idx] + \
#                 max(self.tree[idx * 2], self.tree[idx * 2 + 1])

#     def book(self, start: int, end: int) -> int:
#         self.update(start, end - 1, 0, 100, 1)
#         print(self.tree, self.lazy, sep='\n')
#         return self.tree[1]
