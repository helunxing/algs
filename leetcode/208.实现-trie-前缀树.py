#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (56.92%)
# Total Accepted:    5.2K
# Total Submissions: 9.2K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#
# 示例:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");
# trie.search("app");     // 返回 true
#
# 说明:
#
#
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。
#
#
#


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.p = [None]*26
        self.end = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self
        for letter in word:
            num = ord(letter)-ord('a')
            if not curr.p[num]:
                curr.p[num] = Trie()
            curr = curr.p[num]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self
        for letter in word:
            curr = curr.p[ord(letter)-ord('a')]
            if not curr:
                return False
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self
        for letter in prefix:
            curr = curr.p[ord(letter)-ord('a')]
            if not curr:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
