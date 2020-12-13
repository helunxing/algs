class Solution:
    def generate(self, numRows: int):
        ans = [[1] for i in range(numRows)]
        for i in range(1, numRows):
            for j in range(2, i+1):
                ans[i].append(ans[i-1][j-2]+ans[i-1][j-1])
            ans[i].append(1)
        return ans
