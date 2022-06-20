class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        l = [0]
        r = [0]
        x = 0
        for i in s:
            if i == '1':
                x += 1
            l.append(x)
        x = 0
        for i in reversed(s):
            if i == '0':
                x += 1
            r.append(x)
        r.reverse()
        ans = len(s)
        for i in range(len(s)):
            ans = min(ans, l[i] + r[i+1])
        return ans
