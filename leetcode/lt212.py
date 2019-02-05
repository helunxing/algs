import collections


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

END_OF_WORD = "#"


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        if not words:
            return []

        ans = set()
        root = collections.defaultdict()

        # 建立字典树
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[END_OF_WORD] = END_OF_WORD

        # 在当前格在字典树中的情况下，在周围搜索下个字符
        def DFS(i, j, curr_word, curr_dict):
            curr_word += board[i][j]
            curr_dict = curr_dict[board[i][j]]

            if END_OF_WORD in curr_dict:
                ans.add(curr_word)

            temp, board[i][j] = board[i][j], "@"
            for k in range(4):
                x, y = i+dx[k], j+dy[k]
                if 0 <= x < m and 0 <= y < n \
                        and board[x][y] in curr_dict and board[x][y] != "@":
                    DFS(x, y, curr_word, curr_dict)
            board[i][j] = temp

        m, n = len(board), len(board[0])

        # 从每个格开始DFS
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    DFS(i, j, "", root)

        return list(ans)
