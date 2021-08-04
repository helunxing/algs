class Solution1(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # dp[n][m][0]=max
        #     dp[n-1][m-1][1]+prices[n]
        #     dp[n-1][m][0]
        # or  0
        # dp[n][m][1]=max
        #     dp[n-1][m-1][0]-prices[n]
        #     dp[n-1][m][1]
        # or  -prices[n]
        # days n, deal m, have o

        if not prices:
            return 0

        n = len(prices)
        if k >= n >> 1:
            sum = 0
            for i, j in zip(prices[:-1], prices[1:]):
                sum += j-i if j > i else 0
            return sum

        dphave = [[0 for j in range(k+1)] for i in range(n)]
        dpnot = [[0 for j in range(k+1)] for i in range(n)]

        for i in range(n):
            dphave[i][0] = -prices[i]
            for j in range(1, k+1):
                if i:
                    dpnot[i][j] = max(
                        dpnot[i-1][j],
                        dphave[i-1][j]+prices[i])
                    dphave[i][j] = max(  # 需要在买入时计算交易次数，可能与k，n循环位置有关
                        dphave[i-1][j],
                        dpnot[i-1][j-1]-prices[i])
                else:
                    dphave[i][j] = -prices[i]
        return dpnot[n-1][k]

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        l = len(prices)

        if k >= l << 1:
            s = 0
            for n, c in zip(prices[1:], prices[:-1]):
                s += n-c if n > c else 0
            return s

        dp = [[[0]*(k+1) for i in range(l)] for j in range(2)]
        # 0有股票，1没股票；日期；交易次数
        for d in range(l):
            dp[1][d][0] = -prices[d]
            for t in range(1, k+1):
                if d:
                    dp[0][d][t] = max(
                        dp[1][d-1][t-1]+prices[d],
                        dp[0][d-1][t])
                    dp[1][d][t] = max(
                        dp[0][d-1][t]-prices[d],
                        dp[1][d-1][t])
                else:
                    dp[1][d][t] = -prices[d]

        return dp[0][l-1][k]
