from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        d = {'I': 1, 'D': -1}
        cur = 0
        ans = [0]
        used = set([0])
        for i in s:
            k = d[i]
            while cur in used:
                cur += k
            ans.append(cur)
            used.add(cur)
        m = min(ans)
        return [x - m for x in ans]
