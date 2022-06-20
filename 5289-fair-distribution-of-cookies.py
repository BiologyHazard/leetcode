from itertools import product
from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        ans = 1 << 20
        cookies.sort()
        for p in product(range(k), repeat=n-1):
            children = [0 for _ in range(k)]
            children[0] = cookies[0]
            for i, s in enumerate(p):
                children[s] += cookies[i+1]
            ans = min(ans, max(children))
        return ans
