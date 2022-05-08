from typing import List
from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        GENES = ['A', 'C', 'G', 'T']
        q = deque([(start, 0)])
        vis = set([1])
        while q:
            gene, dis = q.popleft()
            for i in range(8):
                for acgt in GENES:
                    if acgt != gene[i]:
                        new_gene = gene[:i] + acgt + gene[i+1:]
                        if not new_gene in vis and new_gene in bank:
                            if new_gene == end:
                                return dis + 1
                            vis.add(new_gene)
                            q.append((new_gene, dis + 1))
                            # print(new_gene)

        return -1
