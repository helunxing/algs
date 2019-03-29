class Solution1903:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        l, r = 1, x
        while True:
            m = l+(r-l)//2
            if m > x//m:
                r = m-1
            else:
                if m+1 > x//(m+1):
                    return m
                else:
                    l = m+1


s = Solution1903()
print(s.mySqrt(8))
print(s.mySqrt(4))
print(s.mySqrt(5))
print(s.mySqrt(1))


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
