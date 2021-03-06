#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (51.54%)
# Total Accepted:    25.9K
# Total Submissions: 50.2K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
#


class Solution0:
    def isAnagram(self, s: str, t: str) -> bool:
        d = [0]*26
        for i in s:
            d[ord(i)-ord('a')] += 1

        for i in t:
            d[ord(i)-ord('a')] -= 1

        ans = True
        for i in d:
            ans &= not i
        return ans


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnts = [0]*26
        for c in s:
            cnts[ord(c)-ord('a')] += 1
        for c in t:
            cnts[ord(c)-ord('a')] -= 1
        for i in cnts:
            if i:
                return False
        return True
