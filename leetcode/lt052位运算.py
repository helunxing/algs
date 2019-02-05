class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.count = 0
        self.focus = (1 << n)-1
        # 1左移n位减一，只保留n位数字

        def DFS(row, col, pie, na):
            if row >= n:
                self.count += 1
                return

            # 得到空位
            bits = ~(col | pie | na) & self.focus

            while bits > 0:
                p = bits & -bits
                DFS(row+1, col | p, (pie | p) << 1, (na | p) >> 1)
                bits &= bits-1

        DFS(0, 0, 0, 0)

        return self.count
