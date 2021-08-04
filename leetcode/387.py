class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = [0]*26
        for i, x in enumerate(s):
            d[ord(x)-ord('a')] += 1

        for i, x in enumerate(s):
            if d[ord(x)-ord('a')] == 1:
                return i

        return -1
