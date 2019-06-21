class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # 02
        if not M:
            return 0
        n = len(M)
        group = [i for i in range(n)]

        def findr(i):
            r = i
            while group[r] != r:
                r = group[r]
            while group[i] != r:
                i, group[i] = group[i], r
            return r

        def merge(i, j):
            ri, rj = findr(i), findr(j)
            if ri != rj:
                group[ri] = group[rj]

        for i in range(n):
            for j in range(n):
                if not M[i][j]:
                    continue
                merge(i, j)

        ng = 0
        for i in range(n):
            if group[i] == i:
                ng += 1
        return ng
        # 22


class Solution2(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        roots = [i for i in range(n)]

        def find_root(stu_num):
            root = stu_num
            while root != roots[root]:
                root = roots[root]
            i = stu_num
            while i != roots[root]:
                tmp = roots[i]
                roots[i] = roots[root]
                i = tmp
            return root

        def union(p, q):
            roots[find_root(p)] = roots[find_root(q)]

        def connected(p, q):
            return find_root(p) == find_root(q)

        for i in range(n):
            for j in range(n):
                if M[i][j] and not connected(i, j):
                    union(i, j)

        groups = set()

        for i in range(n):
            groups.add(find_root(i))

        return len(groups)

        # return roots


s = Solution()
groups = s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
roots = s.findCircleNum([
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
pass
