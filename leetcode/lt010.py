class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}

        def dp(i, j):
            if (i, j) not in mem:
                if j == len(p):
                    ans = i == len(s)
                else:
                    fst_m = i < len(s) and p[j] in {s[i], '.'}
                    if j < len(p)-1 and p[j+1] == '*':
                        ans = dp(i, j+2) or fst_m and dp(i+1, j)
                    else:
                        ans = fst_m and dp(i+1, j+1)
                mem[i, j] = ans
            return mem[i, j]

        return dp(0, 0)


s = Solution()
ans = s.isMatch("aaa", "ab*a*c*a")
ans = s.isMatch("aa", "a")
ans = s.isMatch("aa", "a*")
ans = s.isMatch("ab", ".*")
ans = s.isMatch("aab", "c*a*b")
ans = s.isMatch("issippi", "is*p*.")
ans = s.isMatch("issippi", "is*ip*.")


class Solution_fail2:
    def isMatch(self, s: str, p: str) -> bool:
        q, ast = [], set()
        for i, x in enumerate(p):
            if x == '*':
                ast.add(len(q)-1)
            else:
                q.append(x)

        def f(t, r):
            # 比较下标已经到了结束时的情况
            if t == len(s) and r == len(q):
                return True
            elif t >= len(s) and r < len(q) \
                    or t < len(s) and r >= len(q):
                return False

            # *的情况
            if r in ast:
                os = 0
                if r == len(q)-1:
                    while t+os < len(s) and comp(t+os, r):
                        os += 1
                    return comp(t+os, r+1)
                while t+os < len(s):
                    # 可重复零或若干次
                    if f(t+os, r+1):
                        return True
                    os += 1
                    if not comp(t+os, r):
                        return f(t+os, r+1)
                return False
            # 非*的情况
            else:
                if comp(t, r):
                    return f(t+1, r+1)
                else:
                    return False

        def comp(a, b):
            if a < len(s) and b < len(q):
                return True if s[a] == q[b] or q[b] == '.' else False
            elif a == len(s) and b == len(q):
                return True
            elif a >= len(s) and b == len(q) \
                    or a == len(s) and b >= len(q):
                return False
            else:
                return True

        return f(0, 0)


class Solution_fail:
    def isMatch(self, s: str, p: str) -> bool:
        s_ = 0
        p_ = 0

        def comp(a, b):
            return True if a == b or b == '.' else False

        while s_ < len(s):
            if p_ == len(p):
                return False
            if p_+1 < len(p) and p[p_+1] == '*':
                # 通配状态，可以匹配零次或者一次
                while s_ < len(s) and comp(s[s_], p[p_]):
                    s_ += 1
                p_ += 2
            elif s_ < len(s) and p_ < len(p):
                if comp(s[s_], p[p_]):
                    s_ += 1
                    p_ += 1
                else:
                    return False

        while p_+1 < len(p) and p[p+1] == '*':
            p_ += 2

        return True if p_ == len(p) else False
