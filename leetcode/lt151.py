# 2019年3月3日写，solution1也是正确的。
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''
        tmp = ''
        l = len(s)
        i = l-1
        while i >= 0:
            if s[i] == ' ':
                while i >= 0 and s[i] == ' ':
                    i -= 1
                tmp += ' '
            else:
                tmp += s[i]
                i -= 1

        ans = ''
        l = len(tmp)
        i = 0
        while i < l:
            ans += ' ' if ans else ''
            sta = i
            while i < l and tmp[i] != ' ':
                i += 1
            end = i
            i -= 1
            while i >= sta and tmp[i] != ' ':
                ans += tmp[i]
                i -= 1
            i = end+1

        return ans


s = Solution()
s.reverseWords('   Hello    world  ')


class Solution1:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''
        i = len(s)-1
        ans = ''

        while i >= 0:
            ans += ' ' if ans else ''
            if s[i] == ' ':
                while i > 0 and s[i] == ' ':
                    i -= 1
                if i == 0 and s[i] == ' ':
                    break
            j = i
            while j > 0 and s[j] != ' ':
                j -= 1
            next = j-1
            j += 1 if s[j] == ' ' else 0
            while j <= i:
                ans += s[j]
                j += 1
            i = next
        return ans


class Solution_fail:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''

        i, j = 0, len(s)-1
        # 去除结尾的空格
        while j > 0 and s[j] == ' ':
            j -= 1

        while i < j:
            if s[j] == ' ':
                while j > 0 and s[j-1] == ' ':
                    j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        i, j = 0, 0

        while True:
            while j < len(s)-1 and s[j] != ' ':
                j += 1
            next = j+1
            j -= 1 if s[j] == ' ' else 0
            while i < j:
                s[i], s[j] = s[j], s[i]
                j -= 1
                i += 1
            i, j = next, next
            if next >= len(s) or s[i] == s[j] == ' ':
                break

        j = len(s)-1
        while s[j] == ' ':
            j -= 1
        return s[:j+1]
