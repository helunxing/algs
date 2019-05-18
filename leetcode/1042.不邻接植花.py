import collections


class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        for p in paths:
            d[p[0]].append(p[1])
            d[p[1]].append(p[0])

        res = [-1 for _ in range(N+1)]

        for i in d.keys():
            occ = [0 for _ in range(5)]
            for nei in d[i]:
                if res[nei] != -1:
                    occ[res[nei]] = 1

            for color_i in range(1, 5):
                if not occ[color_i]:
                    res[i] = color_i
                    break

        for i in range(len(res)):
            if res[i] == -1:
                res[i] = 1

        return res[1:]


class Solution_time_out:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:

        self.ansed = False
        color = [0]*N
        self.ans = []
        conn = collections.defaultdict(list)
        for path in paths:
            conn[path[0]-1].append(path[1]-1)
            conn[path[1]-1].append(path[0]-1)

        def dfs(num):
            if num >= N:
                self.ansed = True
                self.ans = color[:]
                return
            if not conn[num]:
                dfs(num+1)
            for want_color in range(1, 5):
                can_use = True
                for ced_gar_num in conn[num]:
                    if color[ced_gar_num] == want_color:
                        can_use = False
                        break
                if can_use:
                    tmp = color[num]
                    color[num] = want_color
                    dfs(num+1)
                    color[num] = tmp

        dfs(0)
        return self.ans
