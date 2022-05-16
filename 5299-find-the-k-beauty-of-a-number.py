class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        ans = 0
        for i in range(n - k + 1):
            if int(s[i:i+k]) != 0 and num % int(s[i:i+k]) == 0:
                ans += 1
        return ans
