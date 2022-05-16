class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if k < 1:
            return 0

        d = {}
        chrs = 0
        stai = 0
        res = 0

        for i, bit in enumerate(s):
            if bit not in d:
                d[bit] = 0

            if not d[bit]:
                chrs += 1
            d[bit] += 1

            while chrs > k:
                stachr = s[stai]
                stai += 1
                d[stachr] -= 1
                if not d[stachr]:
                    chrs -= 1
            res = max(res, i+1-stai)

        return res


# 386 · 最多有k个不同字符的最长子字符串
# 算法
# 中等
# 通过率
# 30%

# 题目题解笔记讨论排名
# 描述
# 给定字符串S，找到最多有k个不同字符的最长子串T。

class Solution2:
    # @param s : A string
    # @return : An integer

    def lengthOfLongestSubstringKDistinct(self, s, k):

        if k == 0 or len(s) == 0:
            return 0

        char_set = {}
        left, right = 0, 0
        cnt, ans = 0, 0

        while right < len(s):
            # 统计right指向的字符
            # 当字符在窗口内第一次出现时，字符种类数+1，该字符出现次数+1
            if s[right] not in char_set or char_set[s[right]] == 0:
                cnt += 1
                char_set.setdefault(s[right], 0)
            char_set[s[right]] += 1
            right += 1

            # 向右移动left，保持窗口内只有k种不同的字符
            while cnt > k:
                char_set[s[left]] -= 1
                if char_set[s[left]] == 0:
                    cnt -= 1
                left += 1
            # 更新答案
            ans = max(ans, right - left)

        return ans
