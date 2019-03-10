class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        n = len(A)
        if not n:
            return 0
        A.sort()
        fu = 0
        havezero = False
        ans = 0
        absmin = abs(A[0])
        for i in A:
            if i < 0:
                fu += 1
            if not i:
                havezero = True
            absmin = abs(i) if abs(i) < absmin else absmin

        if K < fu:
            for i in A:
                ans += -i if K > 0 else i
                K -= 1
        else:
            for i in A:
                ans += i if i >= 0 else -i
            if (K-fu) & 1 and n and not havezero:
                ans += -absmin*2
        return ans
