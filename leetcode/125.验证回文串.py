#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (38.75%)
# Total Accepted:    30.5K
# Total Submissions: 78.5K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
#
#
# 示例 2:
#
# 输入: "race a car"
# 输出: false
#
#
#


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s)-1
        while l <= r:
            if not (ord('a') <= ord(s[l]) <= ord('z')
                    or ord('0') <= ord(s[l]) <= ord('9')):
                l += 1
            elif not (ord('a') <= ord(s[r]) <= ord('z')
                      or ord('0') <= ord(s[r]) <= ord('9')):
                r -= 1
            else:
                if ord(s[l]) == ord(s[r]):
                    l += 1
                    r -= 1
                else:
                    return False
        return True
        
