class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        tmp = min(A)
        ans = 0
        for i in str(tmp):
            ans += int(i)
        return 0 if ans & 1 else 1
