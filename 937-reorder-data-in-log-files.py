from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def key(log: str) -> tuple:
            a, b = log.split(' ', 1)
            return (0, b, a) if b[0].isalpha() else (1,)

        return sorted(logs, key=key)
