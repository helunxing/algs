class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [[0, 0], [0, 0]]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            x, y = i % 2, (i-1) % 2
            dp[x][0] = max(dp[y][0], dp[y][1]+prices[i])
            dp[x][1] = max(dp[y][0]-prices[i], dp[y][1])
        return dp[(len(prices)-1) % 2][0]
