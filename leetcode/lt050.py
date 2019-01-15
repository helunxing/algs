class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        self.d = {}
        self.x = x
        if n < 0:
            return 1/self.comp(n)
        else:
            return self.comp(n)

    def comp(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return self.x
        y = self.d.setdefault(n/2, self.comp(n/2))
        if n % 2 == 0:
            return y*y
        else:
            return y*y*self.x
