#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        breakp, max_len = [0], 0
        for word in wordDict:
            max_len = max(len(word), max_len)

        for i in range(len(s) + 1):
            for j in breakp:
                if i-j <= max_len and s[j:i] in wordDict:
                    breakp.append(i)
                    break
        return breakp[-1] == len(s)


class Solution_dfs_faild:
    def __init__(self):
        self.tree = [None]*26
        self.end = False

    def insert(self, word):
        curr = self
        for char in word:
            num = ord(char)-ord('a')
            if not curr.tree[num]:
                curr.tree[num] = Solution()
            curr = curr.tree[num]
        curr.end = True

    def wordBreak(self, s: str, wordDict) -> bool:
        self.top = self
        for word in wordDict:
            self.insert(word)

        self.finded = False

        def chr2num(c):
            return ord(c)-ord('a')

        def search(sta):
            if sta == len(s):
                self.top.finded = True
                return
            curr = self
            offset = sta
            while curr:
                if self.top.finded or offset == len(s):
                    return
                curr = curr.tree[chr2num(s[offset])]
                offset += 1
                if curr and curr.end:
                    search(offset)
                    break

        search(0)

        return self.finded
