class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, str):
        # write your code here
        self.nums = set([i for i in range(1, n+1)])
        self.res = 0
        self.ansed = False

        def dfs(sta):
            if self.ansed:
                return
            if sta == len(str):
                self.res = self.nums.pop()
                self.ansed = True
                return
            if str[sta] == '0':
                return
            end = sta+1
            while end <= sta+2:
                nu = int(str[sta:end])
                if nu in self.nums:
                    self.nums.remove(nu)
                    dfs(end)
                    self.nums.add(nu)
                end += 1
        dfs(0)
        return self.res


class Solution2:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, str):
        # write your code here
        l = len(str)
        s = set([i for i in range(1, n+1)])
        self.ansed = False
        self.res = 0

        def dfs(pos):
            if self.ansed:
                return
            if pos == l:
                if len(s) == 1:
                    self.ansed = True
                    self.res = list(s)[0]
                return

            if pos < l-1:
                dou = int(str[pos:pos+2])
                if dou <= n and dou in s:
                    s.remove(dou)
                    dfs(pos+2)
                    s.add(dou)

            sin = int(str[pos:pos+1])
            if sin <= n and sin in s:
                s.remove(sin)
                dfs(pos+1)
                s.add(sin)

        dfs(0)

        return self.res
