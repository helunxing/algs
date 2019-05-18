class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        gro = [i for i in range(26)]

        def findr(x):
            rootx = x
            while gro[rootx] != rootx:
                rootx = gro[rootx]
            return rootx

        def merg(x, y):
            if findr(x) == findr(y):
                return
            rootx, rooty = findr(x), findr(y)
            if rootx > rooty:
                rootx, rooty = rooty, rootx
            gro[rooty] = rootx

        for i in range(len(A)):
            if A[i] != B[i]:
                merg(ord(A[i])-ord('a'),
                     ord(B[i])-ord('a'))

        ans_chrs = []
        for i in range(len(S)):
            ans_chrs.append(chr(findr(ord(S[i])-ord('a'))+ord('a')))

        return ''.join(ans_chrs)
