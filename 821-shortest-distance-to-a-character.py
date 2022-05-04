from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def calc(s: str, c: str) -> List[int]:
            ans = []
            count = 0x0fffffff
            for i, char in enumerate(s):
                if char == c:
                    count = 0
                else:
                    count += 1
                ans.append(count)
            return ans

        l = calc(s, c)
        r = reversed(calc(reversed(s), c))
        return list(map(min, l, r))
