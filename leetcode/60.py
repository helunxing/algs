class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = ''
        wait = [i for i in range(1, n+1)]
        yu = 1
        for i in range(1, n+1):
            yu *= i
        k -= 1
        for i in range(n, 0, -1):
            yu //= i
            _ = k//yu
            k %= yu
            s += str(wait[_])
            del wait[_]
        return s


s = Solution()
ans = s.getPermutation(3, 3)
ans1 = s.getPermutation(4, 9)
