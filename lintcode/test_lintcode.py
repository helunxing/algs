class Solution:
    """
    @param a: the array a
    @param k: the integer k
    @param target: the integer target
    @return: return the number of legal schemes
    """

    def getAns(self, a, k, target):
        # write your code here
        odd, eve = [], []
        for i in a:
            if i & 1 == 1:
                odd.append(i)
            else:
                eve.append(i)

        odd.sort()
        eve.sort()

        def find(krem, sta, tar, a):
            res = 0
            if krem == 1:
                for i in a[sta:]:
                    if i == tar:
                        res += 1
            elif krem == 2:
                i, j = sta, len(a)-1
                while i < j:
                    tmp = a[i]+a[j]
                    if tmp == tar:
                        if a[i] != a[j]:
                            l, r = 1, 1
                            while i < j and a[i+1] == a[i]:
                                l += 1
                                i += 1
                            while i < j and a[j-1] == a[j]:
                                r += 1
                                j -= 1
                            res += l*r
                        else:
                            res += int((j-i+1)*(j-i)/2)
                        i += 1
                        j -= 1
                    elif tmp < a[i]:
                        i += 1
                    else:
                        j -= 1
            else:
                for i in range(sta, len(a)):
                    res += find(krem-1, i+1, tar-a[i], a)
            return res

        return find(k, 0, target, odd)+find(k, 0, target, eve)


s = Solution()

# n个数的和是K

# print(s.getAns([10, 3, 1, 1], 3, 5))
print(s.getAns([8, 1, 5, 5, 4, 7, 2, 1, 5, 8,
                1, 4, 1, 3, 7, 3, 5, 3, 6, 8], 4, 8))
# 34
# assert  == 1


class DFS:
    """
    @param a: the array a
    @param k: the integer k
    @param target: the integer target
    @return: return the number of legal schemes
    """

    def dfs(self, start, count, flag, sum):
        if count <= 0:
            if sum == 0:
                self.result += 1
            return
        for i in range(start, self.n):
            if flag == -1 or flag == (self.b[i] & 1):
                self.dfs(i + 1, count - 1, self.b[i] & 1, sum - self.b[i])

    def getAns(self, a, k, target):
        # write your code here
        self.n = len(a)
        self.b = a[:]
        self.result = 0
        self.dfs(0, k, -1, target)
        return self.result


class huishuo:
    def getAns(self, a, k, target):
        # write your code here
        a.sort()
        odd = list(filter(lambda x: x % 2 == 1, a))
        even = list(filter(lambda x: x % 2 == 0, a))
        cnt = 0

        def dfs(arr, idx, m, n, t):
            nonlocal cnt
            if t == target:
                cnt += 1 if m == k else 0
                return
            for i in range(idx, n):
                if t + arr[i] <= target:
                    dfs(arr, i + 1, m + 1, n, t + arr[i])

        m, n = len(odd), len(even)
        if m >= k:
            dfs(odd, 0, 0, m, 0)
        if n >= k:
            dfs(even, 0, 0, n, 0)
        return cnt


class dp:
    """
    @param a: the array a
    @param k: the integer k
    @param target: the integer target
    @return: return the number of legal schemes
    """

    def getAns(self, A, K, target):
        if target > sum(A):
            return 0
        # dp[i][j][k][l] for first i numbers, using j odd number and k even number generate sum l
        dp = [[[[0] * (target + 1) for k in range(K + 1)]
               for j in range(K + 1)] for i in range(len(A) + 1)]
        dp[0][0][0][0] = 1
        for i in range(1, len(A) + 1):
            for j in range(K + 1):
                for k in range(K + 1):
                    for l in range(target + 1):
                        dp[i][j][k][l] = dp[i - 1][j][k][l]
                        if A[i - 1] % 2 == 1 and j > 0 and l - A[i - 1] >= 0:
                            dp[i][j][k][l] += dp[i - 1][j - 1][k][l - A[i - 1]]
                        elif A[i - 1] % 2 == 0 and k > 0 and l - A[i - 1] >= 0:
                            dp[i][j][k][l] += dp[i - 1][j][k - 1][l - A[i - 1]]
        return dp[len(A)][K][0][target] + dp[len(A)][0][K][target]
