#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿的个数
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (42.01%)
# Total Accepted:    11.8K
# Total Submissions: 28.1K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给定一个由 '1'（陆地）和
# '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
#
# 输出: 1
#
#
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
#
# 输出: 3
#
#
#


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        islands = set()

        def find(x, y, new_island):
            grid[x][y] = '0'
            if new_island:
                islands.add(x*len(grid[0])+y)
            for k in range(4):
                i, j = dx[k]+x, dy[k]+y
                if 0 <= i < len(grid) and 0 <= j < len(grid[0])\
                        and grid[i][j] == '1':
                    find(i, j, False)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    find(i, j, True)

        return len(islands)
