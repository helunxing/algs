class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(s):
            if not s:
                return False
            if s == '0':
                return True
            return True if s[0] != '0' and 0 <= int(s) < 256 else False

        l = len(s)
        if not 3 < l < 13:
            return []

        ans = []
        for i in range(l):
            for j in range(i+1, l):
                for k in range(j+1, l):
                    if valid(s[:i+1]) and \
                       valid(s[i+1:j+1]) and \
                       valid(s[j+1:k+1]) and \
                       valid(s[k+1:]):
                        ans.append(s[:i+1]+'.' +
                                   s[i+1:j+1] + '.' +
                                   s[j+1:k+1]+'.' +
                                   s[k+1:])

        return ans
