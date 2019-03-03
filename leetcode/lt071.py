class Solution:
    def simplifyPath(self, path: str) -> str:
        # 47
        # 1 去最后的斜杠
        # 2 多余的
        def isl(x):
            return ord('a') <= ord(x) <= ord('z')
        deque = []
        s = ''
        for word in path+'/':
            if word == '/':
                if s == '..':
                    if len(deque):
                        deque.pop()
                elif s == '.' or s == '':
                    pass
                else:
                    deque.append(s)
                s = ''
            else:
                s += word
        ans = ''
        for fold in deque:
            ans += '/'+fold
        return ans if ans else '/'
        # 34
