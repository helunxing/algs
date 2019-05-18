class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        border = pow(10, 6)
        b = set([tuple(p) for p in blocked])
        self.ans = True

        self.curr, passed, tar = [tuple(source)], set(), tuple(target)

        def bfs():
            if len(passed) > 20000:
                return
            if not self.curr:
                self.ans = False
                return

            next = set()
            for p in self.curr:
                for k in range(4):
                    x, y = p[0]+dx[k], p[1]+dy[k]
                    if 0 <= x < border and 0 <= y < border and \
                            (x, y) not in passed and (x, y) not in b:
                        next.add((x, y))
                passed.add(p)

            if tar in next:
                return
            self.curr = list(next)
            bfs()

        bfs()
        if self.ans:
            self.curr, passed, tar = [tuple(target)], set(), tuple(source)
            bfs()

        return self.ans
