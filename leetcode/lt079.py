class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        passed = [[False for i in range(len(board[0]))]
                  for j in range(len(board))]
        way = []

        def solve(i, j, n):  # 功能：检查[i,j]是否等于下标为n的字母，等于且未结尾的话向下搜索
            if n > len(word)-1:
                return True
            if n == len(word)-1 and board[i][j] == word[n] and not passed[i][j]:
                return True
            if passed[i][j] or board[i][j] != word[n]:
                return False
            # if n == len(word):
            #     return True
            # 不能使用这种出口判断方式，当字母board中只有一个，word也只有一个时，会出错
            temp_ans = False
            process = []
            way.append([i, j])
            passed[i][j] = True
            # 下方不应使用累进或的方法，会造成多余计算
            if i != 0:
                process.append([i-1, j])
            if i != len(board)-1:
                process.append([i+1, j])
            if j != 0:
                process.append([i, j-1])
            if j != len(board[0])-1:
                process.append([i, j+1])

            for pair in process:
                if solve(pair[0], pair[1], n+1):
                    temp_ans = True
                    break

            passed[i][j] = False
            del way[-1]
            return temp_ans

        for i in range(len(board)):
            for j in range(len(board[0])):
                if solve(i, j, 0):  # 不应使用累进或的方法，会造成多余计算
                    return True

        return False


s = Solution()
# a = s.exist([
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ], 'ABC')
a = s.exist([
    ['a']
], 'a')
pass
