class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        la, lb = len(A), len(B)
        dp = [[0 for j in range(lb)]for i in range(la)]
        conn = False
        for i in range(la):
            if A[i] == B[0] or conn:
                dp[i][0] = 1
                conn = True
        conn = False
        for j in range(lb):
            if B[j] == A[0] or conn:
                dp[0][j] = 1
                conn = True
        for i in range(1, la):
            for j in range(1, lb):
                if A[i] == B[j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i][j])

        return dp[la-1][lb-1]
