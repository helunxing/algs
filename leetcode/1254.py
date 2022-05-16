from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0 and self.dfs(grid, i, j):
                    res += 1
        return res

    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            # next to edge is not closeIsland
            return False
        if grid[row][col] != 0:
            # itself is water satisfy closeIsland
            return True
        # part of potential closeIsland can seen as water
        grid[row][col] = 2
        b1 = self.dfs(grid, row+1, col)
        b2 = self.dfs(grid, row-1, col)
        b3 = self.dfs(grid, row, col-1)
        b4 = self.dfs(grid, row, col+1)
        return b1 and b2 and b3 and b4
        # if write like below, 
        # may cause more island cause by incomplete treaversal
        # return self.dfs(grid, row-1, col) and self.dfs(grid, row+1, col) and\
        #     self.dfs(grid, row, col-1) and self.dfs(grid, row, col+1)


def test():
    s = Solution()

    assert s.closedIsland([[1, 0, 1],
                           [1, 0, 1],
                           [1, 1, 1]]) == 0

    assert s.closedIsland([[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                           [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                           [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                           [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
                           [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                           [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                           [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                           [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                           [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                           [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]) == 5
