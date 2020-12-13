#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#


class Solution0:
    def removeKdigits(self, num: str, k: int) -> str:
        for i in range(k):
            j = 0
            while j < len(num)-1:
                if num[j] > num[j+1]:
                    break
                j += 1
            num = num[:j]+num[j+1:]
        return str(int(num)) if num else '0'


# 41
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return 0
        while k > 0:
            found = False
            for i in range(len(num)-1):
                if num[i] > num[i+1]:
                    num = num[:i]+num[i+1:]
                    found = True
                    break
            if not found:
                num = num[:-1]
            k -= 1
        return num

# 50
# 56
# 特殊情况：前面有零，0