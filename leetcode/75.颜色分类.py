#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx0, idx2 = 0, n-1
        while idx0 < n and nums[idx0] == 0:
            idx0 += 1

        while idx2 >= 0 and nums[idx2] == 2:
            idx2 -= 1

        i = idx0

        while i <= idx2:
            if nums[i] == 0:
                nums[i], nums[idx0] = nums[idx0], nums[i]
                idx0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[idx2] = nums[idx2], nums[i]
                idx2 -= 1
            else:
                i += 1
