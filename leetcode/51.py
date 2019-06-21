class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        shu, pie, na = set(), set(), set()
        ans = []

        def DFS(row, curr_state):
            if row >= n:
                ans.append(curr_state)
                return
            for col in range(n):
                if row-col in na or col in shu or row+col in pie:
                    continue
                # curr_state.append(col)
                # 这样做太复杂
                shu.add(col)
                na.add(row-col)
                pie.add(row+col)

                DFS(row+1, curr_state+[col])

                shu.remove(col)
                na.remove(row-col)
                pie.remove(row+col)
        DFS(0, [])

        def cre_res(anss):
            matrixs = []
            for ans in anss:
                matrix = []
                for col in ans:
                    matrix.append('.'*col + 'Q' + '.'*(n-col-1))
                matrixs.append(matrix)
            return matrixs
        return cre_res(ans)
