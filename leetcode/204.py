class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        odd = [True]*n
        for i in range(2, int(n**0.5)+1):
            for j in range(i*2, n, i):
                odd[j] = False

        return sum(odd)-2
