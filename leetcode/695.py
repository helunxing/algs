class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        slim = m*n+1
        smax = 0
        if not m:
            return 0
        conn = [[1 for i in range(n)] for j in range(m)]
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

        def a2xy(a):
            return (a-slim)//n, (a-slim) % n

        def xy2a(x, y):
            return x*n+y+slim

        def findroot(x, y):
            a, b = x, y
            while conn[a][b] >= slim:
                a, b = a2xy(conn[a][b])
            # tar = xy2a(a, b)
            # while x != a and y != b:
            #     (x, y), conn[x][y] = a2xy(conn[x][y]), tar
            return a, b

        def getS(x, y):
            a, b = findroot(x, y)
            return conn[a][b]

        def cond(i, j, x, y):
            return findroot(i, j) == findroot(x, y)

        def mer(i, j, x, y):
            if cond(i, j, x, y):
                return
            (ri, rj), (rx, ry) = findroot(i, j), findroot(x, y)
            conn[ri][rj] += conn[rx][ry]
            conn[rx][ry] = xy2a(ri, rj)

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                for k in range(4):
                    x, y = i+dx[k], j+dy[k]
                    if 0 <= x < m and 0 <= y < n and grid[x][y]:
                        mer(i, j, x, y)
                smax = getS(i, j) if getS(i, j) > smax else smax
        return smax


s = Solution()
ans = s.maxAreaOfIsland([[0], [1], [1]])
ans = s.maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0],
                         [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]])


class Solution_fangqi:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 03
        smax = 0
        m, n = len(grid[0]), len(grid)
        slim = m*n+1
        if not m or not n:
            return 0
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        conn = [[1]*m for i in range(n)]
        # conn = [[slim+i+j*m for i in range(m)] for j in range(n)]

        def a2xy(a):
            return (a-slim) % m, (a-slim)//m

        def xy2a(x, y):
            return y*m+x+slim

        def findr(a):
            (x, y), (ansx, ansy) = a2xy(a), a2xy(a)
            while conn[ansx][ansy] >= slim:
                ansx, ansy = a2xy(conn[ansx][ansy])
            tar = xy2a(ansx, ansy)
            while x != ansx and y != ansy:
                (x, y), conn[x][y] = a2xy(conn[x][y]), tar
            return ansx, ansy

        def mer(a, b):
            (xa, ya), (xb, yb) = findr(a), findr(b)
            conn[xa][ya] += conn[xb][yb]
            conn[xb][yb] = xy2a(xa, ya)

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                for k in range(4):
                    x, y = i+dx[k], j+dy[k]
                    if 0 <= x < m and 0 <= y < n and grid[x][y]:
                        mer(xy2a(i, j), xy2a(x, y))
                chax, chay = findr(conn[i][j])
                smax = conn[chax][chay] if conn[chax][chay] > smax else smax

        return smax
