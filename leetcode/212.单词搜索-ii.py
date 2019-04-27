#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

import collections


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        END_WORD = '#'

        ans = set()
        root = collections.defaultdict()

        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, collections.defaultdict())
            node[END_WORD] = END_WORD

        def dfs(i, j, curr_word, curr_dict):
            curr_word += board[i][j]
            curr_dict = curr_dict[board[i][j]]
            if END_WORD in curr_dict:
                ans.add(curr_word)

            temp, board[i][j] = board[i][j], '@'
            for k in range(4):
                x, y = i+dx[k], j+dy[k]
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and\
                        board[x][y] in curr_dict and board[x][y] != '@':
                    dfs(x, y, curr_word, curr_dict)
            board[i][j] = temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root:
                    dfs(i, j, '', root)

        return list(ans)
