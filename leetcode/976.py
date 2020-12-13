class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in reversed(range(len(A)-3)):
            if A[i]+A[i+1] > A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0
