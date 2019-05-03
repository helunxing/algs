#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#


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
