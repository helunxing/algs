class Solution:
    def permute(self, S: str):
        strs = []
        sta, end = 0, 0
        levels = []
        self.res = []

        for i, x in enumerate(S):
            if x == "{":
                sta = i
            if x == "}":
                end = i
            if end < sta:
                if S[end] == "}":
                    end += 1
                strs.append(S[end:sta])
                end = sta
            if sta < end:
                if S[sta] == "{":
                    sta += 1
                strs.append(S[sta:end])
                sta = end
        if S[end] == '}' and S[end+1:]:
            strs.append(S[end+1:])
        if end == 0:
            strs.append(S)

        for s in strs:
            if ',' in s:
                levels.append(s.split(','))
            else:
                levels.append([s])

        def dfs(stmp, l):
            if l == len(levels):
                self.res.append(stmp)
                return
            curr_level = levels[l]
            for s in curr_level:
                dfs(stmp+s, l+1)

        dfs('', 0)
        self.res.sort()
        return self.res


s = Solution()
# s.permute("{a,b}c{d,e}f")
s.permute("abcd")
