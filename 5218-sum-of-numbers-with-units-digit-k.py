class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        p = 0
        for i in range(11):
            p = (k * i) % 10
            if p == (num % 10):
                if i == 0 and num != 0:
                    continue
                if k * i > num:
                    return -1
                return i
        return -1
