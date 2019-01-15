class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        shu, pie, na = set(), set(), set()
        self.ans = 0

        def DFS(row):
            if row >= n:
                self.ans += 1
                return
            for col in range(n):
                if row-col in na or col in shu or row+col in pie:
                    continue
                shu.add(col)
                na.add(row-col)
                pie.add(row+col)

                DFS(row+1)

                shu.remove(col)
                na.remove(row-col)
                pie.remove(row+col)
        DFS(0)

        return self.ans
