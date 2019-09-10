import bisect


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        inds = [[], [], [], []]
        for i, x in enumerate(colors):
            inds[x].append(i)

        res = []
        for tar_i, tar_c in queries:
            if not inds[tar_c]:
                res.append(-1)
                continue
            i = bisect.bisect_left(inds[tar_c], tar_i)
            if i == len(inds[tar_c]):
                tmp = abs(inds[tar_c][i-1]-tar_i)
            elif i == 0:
                tmp = abs(inds[tar_c][i]-tar_i)
            else:
                tmp = min(abs(inds[tar_c][i-1]-tar_i),
                          abs(inds[tar_c][i]-tar_i))
            res.append(tmp)

        return res
