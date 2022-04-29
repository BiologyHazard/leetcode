# Definition for a QuadTree node.
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def subsearch(x1, y1, x2, y2):
            if all(grid[x1][y1] == grid[i][j] for i in range(x1, x2) for j in range(y1, y2)):
                return Node(grid[x1][y1], True, None, None, None, None)
            else:
                xm, ym = (x1+x2)//2, (y1+y2)//2
                return Node(0, False,
                            subsearch(x1, y1, xm, ym),
                            subsearch(x1, ym, xm, y2),
                            subsearch(xm, y1, x2, ym),
                            subsearch(xm, ym, x2, y2))
        x0 = len(grid)
        tree = subsearch(0, 0, x0, x0)
        return tree
