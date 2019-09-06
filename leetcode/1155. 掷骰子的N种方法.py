class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if not d:
            return 0
        dp = [0]*(target+1)
        for i in range(1, f+1):
            if i < target+1:
                dp[i] = 1

        for i in range(2, d+1):  # 掷骰子的个数
            for j in range(target,0,-1):  # 最大点数和
                dp[j] = sum(dp[max(1, j-f):j]) % 1000000007

        return dp[target]


class Solution_fail:  # 此答案错误原因：维度放置错误，且累加结果是不正确的
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for j in range(d)] for i in range(target+1)]
        for i in range(1, min(f+1, target+1)):
            dp[i][0] += 1

        for i in range(1, target+1):
            for j in range(1, f+1):
                if i+j < target+1:
                    for k in range(1, d):
                        dp[i+j][k] += dp[i][k-1]
                        dp[i+j][k] %= 1000000007
        res = 0
        for i in dp[target]:
            res += i
            res %= 1000000007
        return res
