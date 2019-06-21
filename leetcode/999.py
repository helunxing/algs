class Solution:
    def numRookCaptures(self, board: 'List[List[str]]') -> 'int':
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    x, y = i, j
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        ans = 0
        for k in range(4):
            i, j = x, y
            while 0 <= i <= m-1 and 0 <= j <= n-1 and board[i][j] != 'B':
                if board[i][j] == 'p':
                    ans += 1
                    break
                i += dx[k]
                j += dy[k]
        return ans
