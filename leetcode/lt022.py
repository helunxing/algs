class Solution(object):
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
