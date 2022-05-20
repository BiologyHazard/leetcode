from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        def recur(i, s=0, rev=False):
            if i == 0:
                nonlocal ans
                ans.append(s)
                return
            if not rev:
                recur(i-1, s, False)
                recur(i-1, (1 << i-1) + s, True)
            else:
                recur(i-1, (1 << i-1) + s, False)
                recur(i-1, s, True)
        ans = []
        recur(n)
        return ans


print(Solution().grayCode(15))
