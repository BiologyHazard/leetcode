class Solution:
    def digitCount(self, num: str) -> bool:
        c = [0 for _ in range(10)]
        for s in num:
            c[int(s)] += 1
        for i, s in enumerate(num):
            if not c[i] == int(s):
                return False
        return True
