import collections


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d = collections.defaultdict(int)
        for x in C:
            for y in D:
                d[-(x+y)] += 1

        ans = 0
        for x in A:
            for y in B:
                ans += d[x+y]
        return ans


s = Solution()
s.fourSumCount([1, 2],
               [-2, -1],
               [-1, 2],
               [0, 2])
