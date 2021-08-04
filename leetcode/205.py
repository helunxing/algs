class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t, t_s = dict(), dict()
        for c1, c2 in zip(s, t):
            if c1 in s_t and c2 != s_t[c1]:
                return False
            if c2 in t_s and c1 != t_s[c2]:
                return False
            s_t[c1] = c2
            t_s[c2] = c1
        return True
