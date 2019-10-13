class Solution:
    def maxPoints(self, points) -> int:
        def gcd(x, y):
            if x % y:
                return gcd(y, x % y)
            else:
                return x
        same_points = {}
        linear = {}
        l = len(points)
        if l < 3:
            return l

        for i in range(l):
            for j in range(i+1, l):
                p1, p2 = tuple(points[i]), tuple(points[j])
                if p1 == p2:
                    if p1 in same_points:
                        same_points[p1].add(i)
                        same_points[p1].add(j)
                    else:
                        same_points[p1] = set([i, j])
                    continue
                if p1[0] == p2[0]:
                    A, B, C = 1, 0, p1[0]
                elif p1[1] == p2[1]:
                    A, B, C = 0, 1, p1[1]
                else:
                    dx, dy = p1[0]-p2[0], p1[1]-p2[1]
                    if dx < 0:
                        dx, dy = -dx, -dy
                    g = gcd(dx, dy)
                    A, B = dy/g, -dx/g
                    C = -A*p1[0]-B*p1[1]
                pair = (A, B, C)
                if pair in linear:
                    linear[pair].add(i)
                    linear[pair].add(j)
                else:
                    linear[pair] = set([i, j])

        return max([len(s) for s in linear.values()]+[len(s) for s in same_points.values()])
