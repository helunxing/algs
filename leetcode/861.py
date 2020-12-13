class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i in range(len(A)):
            if not A[i][0]:
                self.revR(i, A)

        for i in range(len(A[0])):
            if self.countC(i, A) <= len(A)//2:
                self.revC(i, A)

        ans = 0

        for i in range(len(A[0])):
            ans += 2**(len(A[0])-1-i)*self.countC(i, A)
        return ans

    def countC(self, colN, A):
        ans = 0
        for row in A:
            ans += row[colN]
        return ans

    def revR(self, rowN, A):
        for i in range(len(A[rowN])):
            A[rowN][i] = 0 if A[rowN][i] else 1

    def revC(self, colN, A):
        for i in range(len(A)):
            A[i][colN] = 0 if A[i][colN] else 1
