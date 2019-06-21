class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1]*(amount+1)
        dp[0] = 0

        for i in range(amount+1):
            for j in coins:
                if dp[i] != -1 and i+j <= amount:
                    dp[i+j] = dp[i]+1 if \
                        dp[i]+1 < dp[i+j] or dp[i+j] == -1 \
                        else dp[i+j]

        return dp[amount]
