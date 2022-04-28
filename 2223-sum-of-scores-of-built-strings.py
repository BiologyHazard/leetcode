class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            j = 0
            while j+i < n and s[j+i] == s[j]:
                j += 1
            ans += j
        return ans


if __name__ == '__main__':
    print(Solution().sumScores('azbazbzaz'))
