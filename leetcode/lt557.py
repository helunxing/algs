class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        i, l = 0, len(s)

        while i < l:
            ans += ' ' if ans else ''
            sta = i
            while i < l and s[i] != ' ':
                i += 1
            next = i
            while i > sta:
                i -= 1
                ans += s[i]
            i = next+1

        return ans
        