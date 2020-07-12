class Solution:
    def treeDiameter(self, edges) -> int:
        n = len(edges) + 1
        conn = [[] for i in range(n)]
        scope = [1] * (n)
        res = 0
        # 统计度
        for i, j in edges:
            conn[i].append(j)
            conn[j].append(i)
        # 统计最长
        for i in range(n):
            j, k = conn[i][0], conn[i][-1]
            if len(conn[i]) > 2 or len(conn[j]) > 2 or len(conn[k]) > 2:
                continue
            tmp = scope[i] + scope[j]
            res = max(res, tmp)
            scope[i], scope[j] = tmp, tmp
        # 合并
        for i in range(n):
            if len(conn[i]) <= 2:
                continue
            tmp = []
            for j in conn[i]:
                tmp.append([scope[j], j])
            tmp.sort(reverse=True)
            res = max(res, tmp[0][0] + tmp[1][0])
        return res


s = Solution()
s.treeDiameter([[0, 1], [0, 2]])
s.treeDiameter([[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]])
