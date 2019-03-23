class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda i: (i[0], -i[1]))
        bs = [0]*len(envelopes)
        lest = 0
        for enlp in envelopes:
            lo, hi = 0, lest
            while lo < hi:
                m = lo+(hi-lo)//2
                if bs[m] < enlp[1]:
                    lo = m+1
                else:
                    hi = m
            bs[lo] = enlp[1]
            lest += 1 if lo == lest else 0
        return lest


s = Solution()
ans = s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
pass
ans2 = s.maxEnvelopes([[1, 2], [2, 3], [3, 4], [3, 5], [
    4, 5], [5, 5], [5, 6], [6, 7], [7, 8]])
pass
