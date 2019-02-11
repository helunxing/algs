class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        while not N & 1:
            N = N >> 1

        max = 0
        i = 0

        while N > 0:
            bit = N & 1

            if bit:  # 1
                max = i if i > max else max
                i = 0

            i += 1
            N = N >> 1

        return max
