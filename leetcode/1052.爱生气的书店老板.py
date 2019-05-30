class Solution:
    def maxSatisfied(self, customers, grumpy, X: int) -> int:
        n = len(customers)
        back, frow = 0, 1
        dp = [[0, 0] for i in range(n)]

        dp[0][back] = customers[0] if not grumpy[0] else 0
        dp[-1][frow] = customers[-1] if not grumpy[-1] else 0

        for i in range(1, n):
            dp[i][back] = dp[i-1][back] if grumpy[i] \
                else dp[i-1][back]+customers[i]
            dp[n-1-i][frow] = dp[n-i][frow] if grumpy[n-1-i] \
                else dp[n-i][frow]+customers[n-1-i]

        res = 0
        for i in range(n-X+1):
            tmp = sum(customers[i:i+X])
            tmp += dp[i-1][back] if i != 0 else 0
            tmp += dp[i+X][frow] if i != n-X else 0
            res = max(res, tmp)

        return res


s = Solution()
s.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5],
               [0, 1, 0, 1, 0, 1, 0, 1],
               3)
