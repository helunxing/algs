class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0

        dp = [[0]*n, [-prices[i] for i in range(n)]]
        # 0 不持有最有 1 持有最优

        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1]+prices[i]-fee)
            dp[1][i] = max(dp[1][i-1], dp[0][i-1]-prices[i])

        return dp[0][-1]
