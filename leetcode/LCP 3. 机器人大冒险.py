class Solution:
    def robot(self, command: str, obstacles, x: int, y: int) -> bool:
        ps = set()
        un, rn = 0, 0
        for c in command:
            ps.add((rn, un))
            if c == 'U':
                un += 1
            else:
                rn += 1
        mu = min(x // rn, y // un)
        if (x - mu*rn, y - mu*un) not in ps:
            return False

        def match(x, y):
            mu = min(x // rn, y // un)
            if (x - mu*rn, y - mu*un) in ps:
                return True
            return False

        for ob in obstacles:
            if ob[0] <= x and ob[1] <= y and match(ob[0], ob[1]):
                return False
        return True
