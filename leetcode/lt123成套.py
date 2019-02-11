class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        n=len(prices)
        dp=[[[0 for k in range(2)] for j in range(3)] for i in range(n)]
        
        for i in range(n):
            # dp[i][0][1]=-prices[i]
            for j in range(1,3):
                if i:
                    dp[i][j][0]=max(
                        dp[i-1][j][0],
                        dp[i-1][j][1]+prices[i])
                    dp[i][j][1]=max(
                        dp[i-1][j][1],
                        dp[i-1][j-1][0]-prices[i])
                else:
                    dp[0][j][1]=-prices[0]
        
        return dp[n-1][2][0]
    