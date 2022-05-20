from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(l: List[int]) -> None:
            nonlocal ans
            if len(l) == n:
                ans.append(
                    [''.join(['Q' if j == i else '.' for j in range(n)]) for i in l])
                return
            for i in range(n):
                if all(j != i for j in l) and all(p + j != len(l) + i for p, j in enumerate(l)) and all(p - j != len(l) - i for p, j in enumerate(l)):
                    solve(l + [i])
        ans = []
        solve([])
        return ans
