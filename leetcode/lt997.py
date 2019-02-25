class Solution:
    def findJudge(self, N: 'int', trust: 'List[List[int]]') -> 'int':
        if len(trust) < N-1:
            return -1
        ju = [[0, True] for i in range(N+1)]  # 被多少人信任，信任别人这条是否符合法官
        for pi in trust:
            ju[pi[1]][0] += 1
            ju[pi[0]][1] = False

        for i, hu in enumerate(ju):
            if hu[1] and hu[0] == N-1 and i!=0:
                return i

        return -1
