class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = {}
        ans = 0
        for i in time:
            d[i % 60] = d.setdefault(i % 60, 0)+1
        for i in time:
            d[i % 60] -= 1
            ans += d.setdefault((60-i % 60) % 60, 0)

        return ans
