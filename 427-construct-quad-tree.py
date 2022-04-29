from typing import List

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def ps(x1, y1, x2, y2):
            return (partial_sum[x2][y2] - partial_sum[x2][y1]
                    - partial_sum[x1][y2] + partial_sum[x1][y1])

        def all_one_number(x1, y1, x2, y2):
            sum_ = ps(x1, y1, x2, y2)
            area = (x2-x1) * (y2-y1)
            if sum_ == 0:
                return 0
            elif sum_ == area:
                return 1
            else:
                return -1

        n = len(grid)
        partial_sum = [[0 for j in range(n+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                partial_sum[i][j] = (partial_sum[i-1][j] + partial_sum[i][j-1] -
                                     partial_sum[i-1][j-1] + grid[i-1][j-1])

        def construct_tree(x1, y1, x2, y2):
            a = all_one_number(x1, y1, x2, y2)
            if a == 0:
                return Node(0, True, None, None, None, None)
            if a == 1:
                return Node(1, True, None, None, None, None)
            x_mid = (x1+x2) // 2
            y_mid = (y1+y2) // 2
            # topleft = construct_tree(x1, y1, x_mid, y_mid)
            # topright = construct_tree(x1, y_mid, x_mid, y2)
            # bottomleft = construct_tree(x_mid, y1, x2, y_mid)
            # bottomright = construct_tree(x_mid, y_mid, x2, y2)
            # return Node(0, False, topleft, topright, bottomleft, bottomright)
            return Node(0,
                        False,
                        construct_tree(x1, y1, x_mid, y_mid),
                        construct_tree(x1, y_mid, x_mid, y2),
                        construct_tree(x_mid, y1, x2, y_mid),
                        construct_tree(x_mid, y_mid, x2, y2)
                        )

        return construct_tree(0, 0, n, n)


if __name__ == '__main__':
    print(Solution().construct([[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [
          1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]))
