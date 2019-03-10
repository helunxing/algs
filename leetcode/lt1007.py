class Solution:
    def minDominoRotations(self, A, B) -> int:
        l = len(A)
        keneng = [True]*7
        ans = -1
        for i in range(l):
            for j in range(1, 7):
                keneng[j] &= A[i] == j or B[i] == j

        for i in range(1, 7):
            if keneng[i]:
                a2b, b2a = 0, 0
                for j in range(l):
                    if B[j] != i and A[j] == i:
                        b2a += 1
                    if A[j] != i and B[j] == i:
                        a2b += 1
                a = min(b2a, a2b)
                ans = a if a < ans or ans == -1 else ans
        return ans


s = Solution()
s.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2])
