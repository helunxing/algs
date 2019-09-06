import collections


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int],
                              num_wanted: int, use_limit: int) -> int:
        que = []
        res = 0
        used_l = collections.defaultdict(int)
        for i, x in enumerate(values):
            que.append((x, labels[i]))
        que.sort()
        while num_wanted > 0 and que:
            val, lab = que.pop()
            if used_l[lab] < use_limit:
                used_l[lab] += 1
                res += val
                num_wanted -= 1
        return res


class Solution_fail:
    def largestValsFromLabels(self,
                              values: List[int],
                              labels: List[int],
                              len_wanted: int,
                              uselab_limit: int) -> int:

        self.res = 0
        self.usecnt = collections.defaultdict(int)

        def dfs(i, tmp_len,  tmp_sum):

            if tmp_len <= len_wanted:
                self.res = max(self.res, tmp_sum)
            if tmp_len > len_wanted or i == len(values):
                return

            # use
            if self.usecnt[labels[i]] < uselab_limit:
                self.usecnt[labels[i]] += 1
                dfs(i+1, tmp_len+1, tmp_sum+values[i])
                self.usecnt[labels[i]] -= 1

            # not use
            dfs(i+1, tmp_len, tmp_sum)

        dfs(0, 0, 0)

        return self.res
