class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        shown = set()
        p = list(pattern)
        sl = s.split(' ')
        if len(p) != len(sl):
            return False
        for sam, word in zip(p, sl):
            if sam not in d:
                d[sam] = word
                if word in shown:
                    return False
                shown.add(word)
            elif d[sam] != word:
                return False
        return True
