#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (33.17%)
# Total Accepted:    7.7K
# Total Submissions: 23.2K
# Testcase Example:  '[2,3,-2,4]'
#
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#
#


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp_p, dp_n = [0]*n, [0]*n
        ans = nums[0]
        if nums[0] > 0:
            dp_p[0] = nums[0]
        else:
            dp_n[0] = nums[0]
        for i in range(1, n):
            if nums[i] > 0:
                dp_p[i] = nums[i]*dp_p[i-1] if dp_p[i-1] else nums[i]
                dp_n[i] = nums[i]*dp_n[i-1]
            else:
                dp_p[i] = nums[i]*dp_n[i-1]
                dp_n[i] = nums[i]*dp_p[i-1] if dp_p[i-1] else nums[i]
            ans = max(ans, dp_p[i])
        return ans
