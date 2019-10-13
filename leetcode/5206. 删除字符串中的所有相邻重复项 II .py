class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        return self.helper(s, k)

    def helper(self, s, k):
        self.edited = False
        if len(s) == 1:
            return s

        cont = [[0, 0]]
        sta, end = 0, 1

        def f(sta, end):
            last = cont[-1]
            if end-sta >= k:
                self.edited = True
            now = [sta, sta+(end-sta) % k]

            if last[1] == now[0]:
                cont.pop()
                cont.append([last[0], now[1]])
            else:
                cont.append(now)

        while end < len(s):
            if s[sta] == s[end]:
                end += 1
            else:
                f(sta, end)
                sta = end
                end = sta+1
        f(sta, end)

        res = ''
        for sta, end in cont:
            res += s[sta:end]

        return self.helper(res, k) if self.edited else res
