class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not len(matrix) or not len(matrix[0]):
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[int(matrix[0][i]) for i in range(n)], [0]*n]
        ans = max(dp[0])
        dx, dy = [-1, -1, 0], [0, -1, -1]
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == '1':
                    tmp = []
                    for k in range(3):
                        x, y = i+dx[k], j+dy[k]
                        if 0 <= x < m and 0 <= y < n:
                            tmp.append(dp[x & 1][y])
                        else:
                            tmp.append(0)
                    dp[i & 1][j] = min(tmp)+1
                else:
                    dp[i & 1][j] = 0
                ans = max(dp[i & 1][j], ans)
        return ans*ans
