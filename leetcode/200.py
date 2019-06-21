class Solution(object):
    # 并查集
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def find_root(i, j):
            pass

        isls = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                isls.add(find_root(i, j))
        return len(isls)

    # 朴素搜索
    def floodfill_DFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        islands = set()

        def find(i, j, new_land):
            grid[i][j] = '0'
            if new_land:
                islands.add(i*len(grid[0]) + j)
            for k in range(4):
                x, y = i+dx[k], j+dy[k]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0])\
                        and grid[x][y] == '1':
                    find(x, y, False)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    find(i, j, True)
        return len(islands)


s = Solution()
isl = s.numIslands([["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "1"]])
