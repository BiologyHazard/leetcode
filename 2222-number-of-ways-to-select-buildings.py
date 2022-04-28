class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)

        pre_0s = []
        pre_0 = 0

        for b in s:
            if b == '0':
                pre_0 += 1
            pre_0s.append(pre_0)

        count = 0
        for i, b in enumerate(s):
            if b == '0':
                count += (i + 1 - pre_0s[i]) * \
                    (n - i - 1 - pre_0s[-1] + pre_0s[i])
            else:
                count += (pre_0s[i]) * (pre_0s[-1] - pre_0s[i])
        return count


if __name__ == '__main__':
    print(Solution().numberOfWays('001101'))
