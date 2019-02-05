class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def row_check(row):
            appear = [0 for i in range(10)]
            for i in board[row]:
                num = ord(i)-ord('0')
                if num == -2:
                    continue
                if appear[num] == 0:
                    appear[num] = 1
                else:
                    return False
            return True

        def col_check(col):
            appear = [0 for i in range(10)]
            for i in range(9):
                num = ord(board[i][col])-ord('0')
                if num == -2:
                    continue
                if appear[num] == 0:
                    appear[num] = 1
                else:
                    return False
            return True

        def cell_check(i, j):
            appear = [0 for k in range(10)]
            for row in range(i, i+3):
                for col in range(j, j+3):
                    num = ord(board[row][col])-ord('0')
                    if num == -2:
                        continue
                    if appear[num] == 0:
                        appear[num] = 1
                    else:
                        return False
            return True

        for row in range(9):
            if not row_check(row):
                return False
        for col in range(9):
            if not col_check(col):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not cell_check(i, j):
                    return False

        return True
