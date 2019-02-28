class Solution:
    def evalRPN(self, tokens: 'List[str]') -> 'int':
        # 09
        s_num = []
        edits = ['+', '-', '*', '/']
        for t in tokens:
            if t in edits:
                if t == '+':
                    s_num.append(s_num.pop()+s_num.pop())
                elif t == '-':
                    s_num.append(-1*s_num.pop()+s_num.pop())
                elif t == '*':
                    s_num.append(s_num.pop()*s_num.pop())
                else:
                    tmp = s_num.pop()
                    s_num.append(int(s_num.pop()/tmp))
            else:
                s_num.append(int(t))
        return s_num[0]
        # 37
