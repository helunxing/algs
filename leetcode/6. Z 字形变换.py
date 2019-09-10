class Solution:
    def convert(self, s: str, numRows: int) -> str:

        l = len(s)
        if not l:
            return ''
        if numRows == 1:
            return s
        round = numRows*2-2
        plies = l//round

        rows = numRows
        cols = round*plies+l % round

        arr = [['']*cols for i in range(rows)]
        idx = 0
        i, j = 0, 0
        while idx < l:
            arr[i][j] = s[idx]
            if idx % round < rows-1:
                i += 1
            else:
                j += 1
                i -= 1
            idx += 1

        res = ''
        for i in range(rows):
            res += ''.join(arr[i])

        return res
