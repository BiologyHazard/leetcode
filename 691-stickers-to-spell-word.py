from typing import List
from collections import Counter
from functools import lru_cache


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        @lru_cache(None)
        def dfs(cur: str) -> int:
            if not cur:
                return 0

            res = int(1e20)
            for select in counters:
                if cur[0] not in select:
                    continue
                next = replace(select, cur)
                res = min(res, dfs(next) + 1)
            return res

        # 耗尽Counter删除word里的字符
        def replace(counter: Counter, word: str) -> str:
            for char in counter:
                word = word.replace(char, '', counter[char])
            return word

        counters = [Counter(s) for s in stickers]
        res = dfs(target)
        dfs.cache_clear()
        return res if res != int(1e20) else -1


if __name__ == '__main__':
    print(Solution().minStickers(['hello', 'world'], 'hheellooworld'))
