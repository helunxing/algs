class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                ans += prices[i]-prices[i-1]

        return ans


class Solution1903:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0, -prices[0]], [0, 0]]
        for i in range(1, len(prices)):
            dp[i & 1][0] = max(dp[(i-1) & 1][0], dp[(i-1) & 1][1]+prices[i])
            dp[i & 1][1] = max(dp[(i-1) & 1][0]-prices[i], dp[(i-1) & 1][1])

        return dp[(len(prices)-1) & 1][0]
