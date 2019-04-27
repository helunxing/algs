#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#


class Solution:
    def dfs(self, s):
        if s in self.d:
            return self.d[s]
        res = []
        if not s:
            res.append('')
            return res
        for word in self.wD:
            if s.startswith(word):
                sublist = self.dfs(s[len(word):])
                for subs in sublist:
                    res.append(word + (' ' if subs else '') + subs)
        self.d[s] = res
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.d, self.wD = {}, wordDict

        return self.dfs(s)
