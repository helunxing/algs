#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#


class Solution:
    def calculate(self, s: str) -> int:
        s_sym = []
        s_num = []
        i = 0
        d = {'+': 0, '-': 0, '*': 1, '/': 1}

        def compute(sym):
            if sym == '+':
                s_num.append(s_num.pop()+s_num.pop())
            elif sym == '-':
                s_num.append(-s_num.pop()+s_num.pop())
            elif sym == '*':
                s_num.append(s_num.pop()*s_num.pop())
            else:
                divsor = s_num.pop()
                s_num.append(s_num.pop()//divsor)

        while i < len(s):
            if ord('0') <= ord(s[i]) <= ord('9'):
                tmp = 0
                j = i
                while j < len(s) and ord('0') <= ord(s[j]) <= ord('9'):
                    tmp *= 10
                    tmp += ord(s[j])-ord('0')
                    j += 1
                s_num.append(tmp)
                i = j
                if i >= len(s):
                    break
            if s[i] in d:
                while s_sym and d[s[i]] <= d[s_sym[-1]]:
                    compute(s_sym.pop())
                s_sym.append(s[i])
            i += 1
        while s_sym:
            compute(s_sym.pop())
        return s_num
