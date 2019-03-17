import math


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if not N:
            return 1
        ans = 0
        i = 0
        while N:
            N, rem = divmod(N, 2)
            if not rem:
                ans += math.pow(2, i)
            i += 1
        return int(ans)
