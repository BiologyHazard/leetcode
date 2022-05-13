from typing import List
import math


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.n = n
        lvls = math.floor(math.log2(n)) + 1
        self.parents = [[x] for x in parent]
        for i in range(1, lvls):
            k = 2 ** i
            for node in range(n):
                if self.parents[node][i-1] == -1:
                    p = -1
                else:
                    p = self.parents[self.parents[node][i-1]][i-1]
                self.parents[node].append(p)
        # print(*enumerate(self.parents),sep='\n')

    def getKthAncestor(self, node: int, k: int) -> int:
        if node == -1:
            return -1
        if k == 0:
            return node
        if k > self.n:
            return -1
        if k == 1:
            return self.parents[node][0]
        logk = math.floor(math.log2(k))
        return self.getKthAncestor(self.parents[node][logk], k - 2**logk)


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
