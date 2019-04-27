#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (61.93%)
# Total Accepted:    5.6K
# Total Submissions: 9.1K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
#
#


class Solution:
    def partition(self, s: str):
        ans = []

        def dfs(sta, end, path):
            if sta == len(s):
                ans.append(path[:])
                return
            for sep in range(sta+1, end+1):
                if isPalindrome(sta, sep):
                    path.append(s[sta:sep])
                    dfs(sep, end, path)
                    path.pop()

        def isPalindrome(i, j):
            j -= 1
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        dfs(0, len(s), [])
        return ans


s = Solution()
s.partition("aab")
