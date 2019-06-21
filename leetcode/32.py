import bisect


# s = Solution()
# s.longestValidParentheses('(()()')
# s.longestValidParentheses(')()(())')
# s.longestValidParentheses('()()(()((((()))')


class dp_Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        dp = [0]*len(s)
        max = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == ')':
                    comp = i-1-dp[i-1]  # 比较对象
                    if comp >= 0 and s[comp] == '(':
                        dp[i] = dp[i-1]+2
                        dp[i] += dp[comp-1] if comp-1 >= 0 else 0
                        # 继承比较对象之前可能的有效序列
                else:
                    dp[i] = 2 if i < 2 else dp[i-2]+2
            max = dp[i] if dp[i] > max else max
        return max


class Solution_:
    def longestValidParentheses(self, s: 'str') -> 'int':
        if not s:
            return 0

        n = len(s)
        dp = [[0]*5 for i in range(n)]
        # 0 有效左括号个数  1 半合法长度
        # 2 有效右括号个数  3 半合法长度

        def cal_leg(start, end, step, main_sym, VAL, LEG):
            dp[start-step][VAL] = 1 if s[start-step] == main_sym else 0
            dp[start-step][LEG] = 1 if s[start-step] == main_sym else 0
            for i in range(start, end, step):
                if s[i] == main_sym:
                    dp[i][VAL] = dp[i-step][VAL]+1
                    dp[i][LEG] = dp[i-step][LEG]+1
                else:
                    left = dp[i-step][VAL]-1
                    if left >= 0:
                        dp[i][VAL] = left
                        dp[i][LEG] = dp[i-step][LEG]+1

        cal_leg(1, n, 1, '(', 0, 1)
        cal_leg(n-2, -1, -1, ')', 2, 3)

        def joint(l_n, r_n):  # 左位置 右位置

            vlpN = dp[l_n][0]  # 左有效左括号
            vrpN = dp[r_n][2]  # 右有效右括号

            if vlpN > vrpN:  # 左边应该舍弃的多
                tar = vlpN-vrpN  # 舍弃目标数量
                rag = l_n+1-dp[l_n][1]  # 搜索舍弃位置下标范围
                if tar == 1:
                    i = l_n
                    while dp[i][0] != tar:
                        i -= 1
                    return dp[l_n][1]+dp[r_n][3]-dp[i][1]
                i = rag
                # l_r = bisect.bisect_left(
                #     dp[0][rag:l_n+1], tar)  # 移除位置（leftremove）
                # l_o = l_n-l_r  # 向左偏移量（leftoffset）
                # rem = dp[l_n-l_o][1]  # 被移除串的半合法长度
                if dp[i][0] != tar:
                    while dp[i][0] < tar and l_n > i:
                        i += 1
                return dp[l_n][1]+dp[r_n][3]-dp[i][1]

            elif vlpN < vrpN:  # 右边应该舍弃的多
                tar = vrpN-vlpN  # 舍弃目标数量
                rag = r_n-1+dp[r_n][3]  # 搜索舍弃位置下标范围
                if tar == 1:
                    i = r_n
                    while dp[i][2] != tar:
                        i += 1
                    return dp[l_n][1]+dp[r_n][3]-dp[i][3]
                i = rag
                if dp[i][2] != tar:
                    while dp[i][2] < tar and r_n < i:
                        i -= 1
                return dp[l_n][1]+dp[r_n][3]-dp[i][3]
            else:
                return dp[l_n][1]+dp[r_n][3]

        max = 0
        for i in range(n-1):
            dp[i][4] = joint(i, i+1)
            if dp[i][4] > max:
                max = dp[i][4]

        return max


class Solution_fail:
    def longestValidParentheses(self, s: 'str') -> 'int':
        if not s:
            return 0

        n = len(s)
        dp = [[0]*5 for i in range(n)]
        # 0 有效左括号个数  1 半合法长度
        # 2 有效右括号个数  3 半合法长度

        def cal_leg(start, end, step, main_sym, VAL, LEG):
            dp[start-step][VAL] = 1 if s[start-step] == main_sym else 0
            dp[start-step][LEG] = 1 if s[start-step] == main_sym else 0
            for i in range(start, end, step):
                if s[i] == main_sym:
                    dp[i][VAL] = dp[i-step][VAL]+1
                    dp[i][LEG] = dp[i-step][LEG]+1
                else:
                    left = dp[i-step][VAL]-1
                    if left >= 0:
                        dp[i][0] = left
                        dp[i][1] = dp[i-step][1]+1

        cal_leg(1, n, 1, '(', 0, 1)
        cal_leg(n-2, -1, -1, ')', 2, 3)

        def joint(l_n, r_n):  # 左位置 右位置

            vlpN = dp[l_n][0]  # 左有效左括号
            vrpN = dp[r_n][3]  # 右有效右括号

            if vlpN > vrpN:  # 左边应该舍弃的多
                tar = vlpN-vrpN  # 舍弃目标数量
                rag = l_n+1-dp[l_n][1]  # 搜索舍弃位置下标范围
                l_r = bisect.bisect_left(
                    dp[0][rag:l_n+1], tar)  # 移除位置（leftremove）
                l_o = l_n-l_r  # 向左偏移量（leftoffset）
                rem = dp[l_n-l_o][1]  # 被移除串的半合法长度
            elif l_n < r_n:  # 右边应该舍弃的多
                # rag = _-1+dp[_][3]
                # r_r = bisect.bisect_right(dp[2][_:rag], r_n-l_n)
                # rem = dp[r_r][3]
                # else:
                rem = 0
            return dp[l_o][1]+dp[r_n][3]-1-rem

        max = 0
        for i in range(n-1):
            dp[i][4] = joint(i, i+1)

            if dp[i][4] > max:
                max = dp[i][4]

        return max
