class Solution1903:
    def minimumTotal(self, t) -> int:
        # 31
        if not len(t) or not len(t[0]):
            return 0

        dp = t[-1][:]

        for i in range(len(t)-2, -1, -1):
            for j in range(len(t[i])):
                dp[j] = min(dp[j], dp[j+1])+t[i][j]

        return dp[0]


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        lastl = triangle[0][:]
        for i in range(1, len(triangle)):
            thisl = [lastl[0]+triangle[i][0]]
            for j in range(1, len(triangle[i-1])):
                thisl.append(min(lastl[j], lastl[j-1])+triangle[i][j])
            thisl.append(lastl[-1]+triangle[i][-1])
            lastl = thisl
            thisl = []
        return min(lastl)


s = Solution1903()
ans = s.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]])
pass

# class Solution(object):
#     def minimumTotal(self, triangle):
#         """
#         :type triangle: List[List[int]]
#         :rtype: int
#         """
#         if not triangle:
#             return 0
#         ans = [triangle[0]]
#         for i in range(1, len(triangle)):
#             level = [triangle[i][0]+ans[i-1][0]]
#             for j in range(1, len(triangle[i-1])):
#                 level.append(min(ans[i-1][j], ans[i-1][j-1])
#                              + triangle[i][j])
#             level.append(ans[i-1][-1]+triangle[i][-1])
#             ans.append(level)
#         return min(ans[len(triangle)-1])


# class Solution(object):
#     def minimumTotal(self, triangle):
#         """
#         :type triangle: List[List[int]]
#         :rtype: int
#         """
#         if not triangle:
#             return 0
#         lastl = triangle[0][:]
#         for i in range(1, len(triangle)):
#             thisl = [lastl[0]+triangle[i][0]]
#             for j in range(1, len(triangle[i-1])):
#                 thisl.append(min(lastl[j], lastl[j-1])+triangle[i][j])
#             thisl.append(lastl[-1]+triangle[i][-1])
#             lastl = thisl
#             thisl = []
#         return min(lastl)
