from collections import defaultdict
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        n = len(messages)
        d = defaultdict(int)
        for i in range(n):
            d[senders[i]] += len(messages[i].split())
        return sorted(d.items(), key=lambda x: (x[1], x[0]))[-1][0]
