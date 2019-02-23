class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # if not prices:
        #     return 0
        
        n=len(prices)
        if n<2:
            return 0
        
        dp=[[0,0,-prices[i]] for i in range(2)]
        # 不持股，不持股且在冷冻期，持股
        
        for i in range(1,n):
            # if dp[i-1][1]+prices[i]>dp[i-1][0]:# 卖出不持股盈利多
            # else:# 继承不持股盈利多或持平
            curr,last=i&1,(i-1)&1
            dp[curr][0]=max(dp[last][2]+prices[i],
                            dp[last][0])
            dp[curr][1]=dp[last][0]
            dp[curr][2]=max(dp[last][1]-prices[i],
                            dp[last][2])
        
        return dp[(n-1)&1][0]
    