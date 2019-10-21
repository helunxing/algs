class Solution:
    def probabilityOfHeads(self, prob, target: int) -> float:
        dp = [0.0] * (target+1)
        dp[0] = 1.0

        for i in range(1, len(prob)+1):
            for j in reversed(range(min(i, target)+1)):
                dp[j] = dp[j] * (1 - prob[i-1]) + \
                    (dp[j-1] * prob[i-1] if j > 0 else 0)
        return dp[target]
