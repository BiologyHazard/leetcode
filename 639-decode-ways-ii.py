# class Solution:
#     def numDecodings(self, s: str) -> int:
# n = len(s)
# ans = [1] + [0]*n
# s = list(s)
# for i in range(n):
#     if s[i] == '*':
#         for j in range(1, 10):
#             s[i] = str(j)
#             ans[i+1] += ans[i]
#             if i > 0:
#                 if 10 <= int(''.join(s[i-1:i+1])) <= 26:
#                     ans[i+1] += ans[i-1]
#     else:
#         if s[i] != '0':
#             ans[i+1] += ans[i]
#         if i > 0:
#             if 10 <= int(''.join(s[i-1:i+1])) <= 26:
#                 ans[i+1] += ans[i-1]
# return ans[-1]


class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9 + 7

        def check1digit(ch: str) -> int:
            if ch == "0":
                return 0
            return 9 if ch == "*" else 1

        def check2digits(c0: str, c1: str) -> int:
            if c0 == c1 == "*":
                return 15
            if c0 == "*":
                return 2 if c1 <= "6" else 1
            if c1 == "*":
                return 9 if c0 == "1" else (6 if c0 == "2" else 0)
            return int(c0 != "0" and int(c0) * 10 + int(c1) <= 26)

        n = len(s)
        # a = f[i-2], b = f[i-1], c = f[i]
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = b * check1digit(s[i - 1])
            if i > 1:
                c += a * check2digits(s[i - 2], s[i - 1])
            c %= mod
            a = b
            b = c

        return c
