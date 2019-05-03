#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lts = [nums[0]]
        for i in range(1, len(nums)):
            if lts[-1] < nums[i]:
                lts.append(nums[i])
            else:
                l, r = 0, len(lts)-1
                while l < r:
                    m = l+(r-l)//2
                    if lts[m] < nums[i]:
                        l = m+1
                    else:
                        r = m
                lts[l] = nums[i]
        return len(lts)
