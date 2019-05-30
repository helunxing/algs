#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#


class Solution_timeout:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        n = len(wordList)
        end_idx = -1
        for i in range(n):
            if wordList[i] == endWord:
                end_idx = i
                break
        if end_idx == -1:
            return 0

        paths = [[] for _ in range(n)]
        self.steps = 1

        passed = set()
        self.curr_level = set()

        def diffOneChr(s1, s2):
            res = False
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    if res:
                        return False
                    else:
                        res = True
            return res

        for i in range(n):
            if diffOneChr(wordList[i], beginWord):
                passed.add(i)
                self.curr_level.add(i)
            for j in range(i+1, n):
                if diffOneChr(wordList[i], wordList[j]):
                    paths[i].append(j)
                    paths[j].append(i)

        def bfs():
            if not self.curr_level:
                self.steps = 0
                return
            self.steps += 1
            if end_idx in self.curr_level:
                return
            next_level = set()
            for cn_idx in self.curr_level:
                for nn_idx in paths[cn_idx]:
                    if nn_idx not in passed:
                        next_level.add(nn_idx)
                        passed.add(nn_idx)
            self.curr_level = next_level
            bfs()

        bfs()
        return self.steps


import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        d = collections.defaultdict(list)
        for word in wordList+[beginWord, endWord]:
            for i in range(len(word)):
                k = word[:i]+'_'+word[i+1:]
                d[k].append(word)

        q, visted = collections.deque(), set()
        q.append((beginWord, 1))
        while q:
            word, step = q.popleft()
            if word in visted:
                continue
            visted.add(word)
            if word == endWord:
                return step
            for i in range(len(word)):
                k = word[:i]+'_'+word[i+1:]
                for match in d[k]:
                    if match not in visted:
                        q.append((match, step+1))
        return 0
