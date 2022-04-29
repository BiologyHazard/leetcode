class Solution:
    def countLatticePoints(self, circles) -> int:
        def sqr(x):
            return x*x

        def in_circle(point1, point2, r):
            x1, y1 = point1
            x2, y2 = point2
            return sqr(x1-x2) + sqr(y1-y2) <= sqr(r)

        point_set = set()
        for circle in circles:
            x, y, r = circle
            for i in range(x-r, x+r+1):
                for j in range(y-r, y+r+1):
                    if in_circle((i, j), (x, y), r):
                        point_set.add((i, j))
        return len(point_set)
