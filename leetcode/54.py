class Solution:
    def spiralOrder(self, matrix):
        # 27
        # 0,0的情况
        ans = []
        if not matrix or not len(matrix[0]):
            return ans
        m, n = len(matrix), len(matrix[0])
        # if not m:
        #     return matrix[0]
        # if not n:
        #     return [matrix[i][0] for i in range(m+1)]
        o = (min(m, n)+1)//2  # 圈数
        p = (min(m, n))//2+1  # 奇数最中心圈数
        for i in range(o):
            for j in range(i, n-1-i):
                ans.append(matrix[i][j])
            for j in range(i, m-i):
                ans.append(matrix[j][n-1-i])
            if i != p-1:
                for j in range(n-1-i-1, i, -1):
                    ans.append(matrix[m-1-i][j])
                for j in range(m-1-i, i, -1):
                    ans.append(matrix[j][i])
        # if m == n and not m & 1:
        #     ans.append(matrix[o-1][o-1])
        return ans


s = Solution()
ans = s.spiralOrder([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
ans0 = s.spiralOrder([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
ans1 = s.spiralOrder([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
ans2 = s.spiralOrder([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12]])
ans3 = s.spiralOrder([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 1, 2, 5],
                      [9, 0, 1, 7]])
ans4 = s.spiralOrder([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9],
                      [0, 3, 5]])


# [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
# [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 5], [9, 0, 1, 7]]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 3, 5]]

# [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
# [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# [[2, 3, 4],
#  [5, 6, 7],
#  [8, 9, 10],
#  [11, 12, 13],
#  [14, 15, 16]]
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9, 10, 11, 12]]
# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9, 1, 2, 5],
#  [9, 0, 1, 7]]
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9],
#  [0, 3, 5]]
