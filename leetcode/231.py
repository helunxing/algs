class Solution1903:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return not n & (n-1)


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        n &= n-1
        return not n

# 统计1的个数
# class Solution(object):
#     def isPowerOfTwo(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n < 0:
#             return False
#         count = 0
#         while n:
#             count += n & 1
#             n = n >> 1
#         return count == 1
