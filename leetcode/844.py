class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []
        for i in S:
            if i != '#':
                stack_s.append(i)
            if i == '#' and len(stack_s) > 0:
                del stack_s[-1]

        for i in T:
            if i != '#':
                stack_t.append(i)
            if i == '#' and len(stack_t) > 0:
                del stack_t[-1]

        if len(stack_s) != len(stack_t):
            return False

        for i in range(len(stack_s)):
            if stack_s[i] != stack_t[i]:
                return False

        return True


s = Solution()
s.backspaceCompare('ab#c', 'ad#c')
