class Solution_fail:
    def shipWithinDays(self, weights, D: int) -> int:
        def valid(n):
            count_day = 0
            tmp = 0
            for x in weights:
                if x > n:
                    return False
                if tmp+x > n:
                    tmp = x
                    count_day += 1
                else:
                    tmp += x
            if tmp > 0:
                count_day += 1
            return count_day <= D
        lo, hi = 0, 100000
        while lo < hi:
            m = lo+(hi-lo)//2
            if valid(m):
                hi = m
            else:
                lo = m+1
        return lo


s = Solution_fail()
print(s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
