class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        edge = max(n, m)
        res = ''
        for i in range(edge):
            if m % (i+1) == 0 and n % (i+1) == 0 and str1[:i+1] == str2[:i+1] and \
                    str1 == str1[:i+1]*(m//(i+1)) and str2 == str2[:i+1]*(n//(i+1)):
                res = str1[:i+1]
        return res
