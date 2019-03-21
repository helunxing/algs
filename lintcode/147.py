import math


class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """

    def getNarcissisticNumbers(self, n):
        # write your code here
        ans = []
        if n == 1:
            ans.append(0)
        for i in range(int(math.pow(10, n-1)), int(math.pow(10, n))):
            tmp = 0
            s = str(i)
            for j in range(len(s)):
                tmp += math.pow(int(s[j]), n)
            if tmp == i:
                ans.append(i)
        return ans


s = Solution()
s.getNarcissisticNumbers(1)
pass
