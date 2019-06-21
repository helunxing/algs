class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        cell = [[set() for i in range(3)]for j in range(3)]
        emptys = []
        numbers = set(i for i in range(1, 10))

        def cre_sets():
            for i in range(9):
                for j in range(9):
                    num = ord(board[i][j])-ord('0')
                    if num == -2:
                        emptys.append([i, j])
                        continue
                    row[i].add(num)
                    col[j].add(num)
                    cell[i//3][j//3].add(num)

        def DFS(emptys_num, path):
            if emptys_num >= len(emptys):
                for i in range(len(emptys)):
                    board[
                        emptys[i][0]][
                        emptys[i][1]] = chr(path[i]+ord('0'))
                return

            row_num = emptys[emptys_num][0]
            col_num = emptys[emptys_num][1]

            selable = numbers-(row[row_num] |
                               col[col_num] |
                               cell[row_num//3][col_num//3])

            if not len(selable):
                return

            for i in selable:
                row[row_num].add(i)
                col[col_num].add(i)
                cell[row_num//3][col_num//3].add(i)

                DFS(emptys_num+1, path+[i])

                row[row_num].remove(i)
                col[col_num].remove(i)
                cell[row_num//3][col_num//3].remove(i)

        cre_sets()
        DFS(0, [])
        return


class Solution_sorted(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        cell = [[set() for i in range(3)]for j in range(3)]
        emptys = []
        numbers = set(i for i in range(1, 10))

        def cre_sets():
            for i in range(9):
                for j in range(9):
                    num = ord(board[i][j])-ord('0')
                    if num == -2:
                        continue
                    row[i].add(num)
                    col[j].add(num)
                    cell[i//3][j//3].add(num)

            for i in range(9):
                for j in range(9):
                    num = ord(board[i][j])-ord('0')
                    if num == -2:
                        selable = numbers-(row[i] |
                                           col[j] |
                                           cell[i//3][j//3])
                        emptys.append([i, j, selable])

            emptys.sort(key=lambda x: x[2])

        def DFS(emptys_num, path):
            if emptys_num >= len(emptys):
                for i in range(len(emptys)):
                    board[
                        emptys[i][0]][
                        emptys[i][1]] = chr(path[i]+ord('0'))
                return

            row_num = emptys[emptys_num][0]
            col_num = emptys[emptys_num][1]

            selable = numbers-(row[row_num] |
                               col[col_num] |
                               cell[row_num//3][col_num//3])

            if not len(selable):
                return

            for i in selable:
                row[row_num].add(i)
                col[col_num].add(i)
                cell[row_num//3][col_num//3].add(i)

                DFS(emptys_num+1, path+[i])

                row[row_num].remove(i)
                col[col_num].remove(i)
                cell[row_num//3][col_num//3].remove(i)

        cre_sets()
        DFS(0, [])
        return


s = Solution()
input = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s.solveSudoku(input)
pass
