class Solution:
    def generateMatrix(self, n: int):
        # 05
        if not n:
            return[]
        ans = [[0]*n for i in range(n)]
        if n & 1:
            ans[n//2][n//2] = n*n
        l = 1
        for i in range(n//2):
            for j in range(i, n-i-1):
                ans[i][j] = l
                l += 1
            for j in range(i, n-i-1):
                ans[j][n-1-i] = l
                l += 1
            for j in range(n-1-i, i, -1):
                ans[n-i-1][j] = l
                l += 1
            for j in range(n-1-i, i, -1):
                ans[j][i] = l
                l += 1
        return ans
        # 23


s = Solution()
ans3 = s.generateMatrix(3)
ans2 = s.generateMatrix(2)
ans0 = s.generateMatrix(0)
ans4 = s.generateMatrix(4)
pass
