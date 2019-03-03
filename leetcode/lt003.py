class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 25
        cp = set()  # current present
        ll = 0  # last length
        ma = 0  # max length
        for i in range(len(s)):
            if s[i] in cp:
                ma = len(cp) if len(cp) > ma else ma
                j = len(cp)
                while s[i] in cp:
                    cp.remove(s[i-j])
                    j -= 1
            cp.add(s[i])
        return ma
