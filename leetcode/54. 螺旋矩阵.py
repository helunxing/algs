class Solution_old:
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


class Solution_1910:
    def spiralOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        res = [0]*m*n

        x1, x2, y1, y2 = 0, m-1, 0, n-1

        i = 0
        while x1 <= x2 and y1 <= y2:
            for y in range(y1, y2+1):
                res[i] = matrix[x1][y]
                i += 1
            for x in range(x1+1, x2+1):
                res[i] = matrix[x][y2]
                i += 1
            if x1 < x2 and y1 < y2:
                for y in reversed(range(y1, y2)):
                    res[i] = matrix[x2][y]
                    i += 1
                for x in reversed(range(x1+1, x2)):
                    res[i] = matrix[x][y1]
                    i += 1

            x1 += 1
            x2 -= 1
            y1 += 1
            y2 -= 1

        return res


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

[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
[[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
[[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 5], [9, 0, 1, 7]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 3, 5]]

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
