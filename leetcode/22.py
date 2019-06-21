class Solution(object):
    def generateParenthesis_1903(self, n: int) -> List[str]:
        self.ans = []

        def helper(s, l, r):
            if l == r == 0:
                self.ans.append(s)
            if l > 0:
                helper(s+'(', l-1, r)
            if r > l:
                helper(s+')', l, r-1)

        helper('', n, n)
        return self.ans

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def cre_s(s, left, right):
            if len(s) == 2*n:
                ans.append(s)
                return
            if left < n:
                cre_s(s+'(', left+1, right)
            if right < left:
                cre_s(s+')', left, right+1)

        cre_s('', 0, 0)
        return ans
