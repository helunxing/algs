#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#


class Solution_1905(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        self.res = amount + 1

        def dfs(c, remain, count):
            if not remain:
                self.res = min(self.res, count)

            for i in range(c, len(coins)):
                if coins[i] <= remain < (self.res - count)*coins[i]:
                    dfs(i, remain-coins[i], count+1)

        for i in range(len(coins)):
            dfs(i, amount, 0)

        return self.res if self.res <= amount else -1


class Solution_1905_2(object):
    def coinChange(self, coins, amount):
        self.res = float("inf")
        n = len(coins)
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        if amount < coins[-1]:
            return -1

        def dfs(loc, remain, count):
            if remain == 0:
                self.res = min(self.res, count)
            else:
                for i in range(loc, n):
                    if coins[i] <= remain < coins[i] * (self.res - count):
                        dfs(i, remain - coins[i], count + 1)
        for i in range(n):
            dfs(i, amount, 0)
        return self.res if self.res != float("inf") else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        if amount == 0:
            return 0
        dp = [0]*(amount+1)
        for j in coins:
            if j < len(dp):
                dp[j] = 1
        for i in range(len(dp)):
            for j in coins:
                if 0 < i-j and dp[i-j]:
                    dp[i] = min(dp[i-j]+1, dp[i]) if dp[i] else dp[i-j]+1
        return dp[-1] if dp[-1] else -1
