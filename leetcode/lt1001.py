import collections


class Solution:
    def gridIllumination(self, N: 'int', lamps: 'List[List[int]]', queries: 'List[List[int]]') -> 'List[int]':
        dix = [0, 0, 0, 1, 1, 1, -1, -1, -1]
        diy = [1, -1, 0, 1, -1, 0, 1, -1, 0]
        dx, dy = [1, 0, 1, 1], [0, 1, 1, -1]
        mar = [collections.defaultdict(list) for i in range(4)]
        corr = {}
        open = [True] * len(lamps)

        for i, lamp in enumerate(lamps):
            for j in range(4):
                tar = lamp[0]*dx[j]+lamp[1]*dy[j]
                mar[j][tar].append(i)
            corr[tuple(lamp)] = i
        ans = []
        for q in queries:
            light = False
            for j in range(4):
                tar = q[0]*dx[j]+q[1]*dy[j]
                for k in mar[j][tar]:
                    light |= open[k]
            ans.append(1 if light else 0)
            for j in range(9):
                x, y = q[0]+dix[j], q[1]+diy[j]
                if 0 <= x < N and 0 <= y < N:
                    num = corr.setdefault((x, y), -1)
                    if num != -1:
                        open[num] = False
        return ans
