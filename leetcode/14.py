class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        i = 0
        while True:
            if len(strs[0]) <= i:
                return strs[0][:i]
            for j, s in enumerate(strs):
                if len(s) <= i or s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1


s = Solution()
s.longestCommonPrefix(["flower", "flow", "flight"])
