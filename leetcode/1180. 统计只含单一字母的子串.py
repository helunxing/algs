class Solution:
    def countLetters(self, S: str) -> int:
        l = len(S)
        res = l
        for i in range(l):
            for j in range(i+1, l):
                if S[j] == S[i]:
                    res += 1
                else:
                    break

        return res
