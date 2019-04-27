#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        for i in range(k):
            j = 0
            while j < len(num)-1:
                if num[j] > num[j+1]:
                    break
                j += 1
            num = num[:j]+num[j+1:]
        return str(int(num)) if num else '0'
