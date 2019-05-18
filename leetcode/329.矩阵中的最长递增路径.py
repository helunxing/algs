#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        mem = {}
        for i in range(m):
            for j in range(n):
                mem[i, j] = -1
        longest = 0
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

        def dfs(x, y):
            if mem[x, y] != -1:
                return mem[x, y]
            for k in range(4):
                i, j = x+dx[k], y+dy[k]
                if 0 <= i < m and 0 <= j < n and \
                        matrix[x][y] < matrix[i][j]:
                    mem[x, y] = max(mem[x, y], dfs(i, j)+1)
            if mem[x, y] == -1:
                mem[x, y] = 1
            return mem[x, y]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)
                longest = max(longest, mem[(i, j)])
        return longest
