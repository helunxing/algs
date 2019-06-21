class Solution:
    def old_strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == 0:
            return 0 if len(needle) == 0 else -1

        pmt = self.cra_pmt(needle)
        i = 0
        j = 0
        match = True
        ran = len(haystack)-len(needle)+1
        while i < ran:
            match = False
            j = 0
            while j < len(needle):
                if needle[j] == haystack[i]:
                    match = True
                    i += 1
                    j += 1
                else:
                    if j != 0 and pmt[j-1] != 0:
                        j = pmt[j-1]
                        if len(haystack)-1-j < 0:
                            return -1
                    else:
                        i -= j
                        i += 1
                        break
            if j == len(needle) and match:
                return i-j
            if not match:
                i += 1

        return -1

    def strStr(self, haystack, needle):
        if not len(needle):
            return 0
        pmt = self.cra_pmt(needle)
        i = 0
        ran = len(haystack)-len(needle)+1
        while i < ran:
            j = 0
            while j < len(needle):
                if len(haystack)-i < len(needle)-j-1:
                    return -1
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    if pmt[j]:
                        j = pmt[j]
                    else:
                        i -= j
                        i += 1
                        break
                        # 此处不应该将j置0，而是应该直接退出，需要判断i是否符合范围
            if j == len(needle):
                return i-j
        # 特殊情况：子串长度为0，串长度为0，串长度短于子串
        return -1

    def cra_pmt(self, needle):
        pmt = [0 for i in range(len(needle)+1)]  # partial_match_table
        for i in range(1, len(needle)):
            if needle[i] == needle[pmt[i]]:
                pmt[i+1] = pmt[i]+1
            elif needle[i] == needle[0]:
                pmt[i+1] = 1
        return pmt
    # 无法通过"aabaaabaaac", "aabaaac"，说明该函数用的方法是错误的
    # 最后一个pmt是不正确的


s = lt.Solution()
# print(s.cra_pmt('abcab'))
# print(s.strStr("mississippi", "pi"))
print(s.strStr("aabaaabaaac", "aabaaac"))
# print(s.strStr('aaaaba', 'ba'))
