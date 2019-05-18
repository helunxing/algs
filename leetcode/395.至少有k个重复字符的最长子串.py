#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有K个重复字符的最长子串
#


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0

        for ltrsnum in range(1, 26):
            alp = [0]*26
            i, j = 0, 0
            appltrnum = 0
            morelessthanK = 0
            while j < len(s):
                if appltrnum <= ltrsnum:
                    idx = ord(s[j])-ord('a')
                    if not alp[idx]:
                        appltrnum += 1
                    alp[idx] += 1
                    if alp[idx] == k:
                        morelessthanK += 1
                    j += 1
                else:
                    idx = ord(s[i])-ord('a')
                    if k == alp[idx]:
                        morelessthanK -= 1
                    alp[idx] -= 1
                    if not alp[idx]:
                        appltrnum -= 1
                    i += 1

                if appltrnum == morelessthanK == ltrsnum:
                    ans = max(ans, j-i+1)

        return ans
