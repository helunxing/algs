class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if not s:
        #     return 0
        n = len(s)
        ll, rr, lest = 0, 0, 0
        for i in range(2*n):
            l, r, ltmp = ((i-1)//2, (i+1)//2, 0) \
                if i & 1 else ((i-2)//2, (i+2)//2, 1)
            while 0 <= l < n and 0 <= r < n:
                if s[l] == s[r]:
                    ltmp += 2
                    l -= 1
                    r += 1
                else:
                    break
            ll, rr, lest = (l+1, r-1, ltmp) if ltmp > lest \
                else (ll, rr, lest)
        return s[ll:rr+1]


# s = Solution()
# s.longestPalindrome()


class Solution_error:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        l = len(s)
        dp = [1, 1]
        max_, maxl = 0, 1

        for i in range(1, l):
            last, curr = (i-1) & 1, i & 1
            add1 = dp[last] if s[i-dp[last]+1] == s[i] else 1
            add2 = dp[last]+1 if i-dp[last] >= 0 \
                and s[i-dp[last]] == s[i] else 1
            add3 = dp[last]+2 if i-dp[last] - 1 >= 0 \
                and s[i-dp[last]-1] == s[i] else 1
            dp[curr] = max(add1, add2, add3)
            max_, maxl = (max_, maxl) if maxl > dp[curr] else (i, dp[curr])
        return s[max_-maxl+1:max_+1]

# "babad"
# ""
# "aaabaaaa"
# "bananas"
# "cbbd"
