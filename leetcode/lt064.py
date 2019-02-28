class Solution:
    def minPathSum(self, grid) -> int:
        # 30
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for i in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mi = 0
                if i != m-1 and j != n-1:
                    mi = min(dp[i][j+1], dp[i+1][j])
                elif i == m-1 and j != n-1:
                    mi = dp[i][j+1]
                elif i != m-1 and j == n-1:
                    mi = dp[i+1][j]
                dp[i][j] = mi+grid[i][j]

        return dp[0][0]
