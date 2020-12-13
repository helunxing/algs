class Solution:
    def sortString(self, s: str) -> str:
        b = [0]*26
        for c in s:
            b[ord(c)-ord('a')] += 1

        l = []

        while len(l) < len(s):
            for i in range(26):
                if b[i]:
                    b[i] -= 1
                    l.append(chr(ord('a')+i))
            for i in reversed(range(26)):
                if b[i]:
                    b[i] -= 1
                    l.append(chr(ord('a')+i))

        return ''.join(l)
