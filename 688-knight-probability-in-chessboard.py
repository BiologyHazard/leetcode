class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        DIRECTIONS = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                      (-2, -1), (-1, -2), (1, -2), (2, -1)]
        prob = [[0.0 for j in range(n)] for i in range(n)]
        prob[row][column] = 1.0
        for i in range(k):
            new_prob = [[0.0 for j in range(n)] for i in range(n)]
            for x in range(n):
                for y in range(n):
                    for dx, dy in DIRECTIONS:
                        xx, yy = x+dx, y+dy
                        if 0 <= xx < n and 0 <= yy < n:
                            new_prob[x][y] += prob[xx][yy] / 8
            prob = new_prob
        return sum(map(sum, prob))
