class Solution:
    def removeVowels(self, S: str) -> str:
        yuan = {'a', 'e', 'i', 'o', 'u'}
        i = 0
        while i < len(S):
            if S[i] in yuan:
                S = S[:i]+S[i+1:]
            else:
                i += 1
        return S
