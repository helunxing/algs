class Solution(object):
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
