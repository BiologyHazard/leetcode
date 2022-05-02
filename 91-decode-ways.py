# from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        # 搜索，垃圾
        '''@lru_cache(maxsize=None)
        def calc(begin: int) -> int:
            if begin >= n:
                return 1
            if s[begin] == '0':
                return 0
            if begin == n-1:
                return 1
            if 10 <= int(s[begin:begin+2]) <= 26:
                return calc(begin+2) + calc(begin+1)
            return calc(begin+1)

        n = len(s)
        return calc(0)'''

        # dp，好
        n = len(s)
        ans = [1] + [0]*n
        for i in range(n):
            if s[i] != '0':
                ans[i+1] += ans[i]
            if i > 0:
                if 10 <= int(s[i-1:i+1]) <= 26:
                    ans[i+1] += ans[i-1]
        return ans[-1]
