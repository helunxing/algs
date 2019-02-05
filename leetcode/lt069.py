class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = (left+right)//2
            square = mid*mid
            if square <= x and x < (mid+1)*(mid+1):
                return mid
            elif square < x:
                left = mid+1
            else:
                right = mid-1
        return 0


s = Solution()
s.mySqrt(9)
