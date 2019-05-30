#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#

import random


class Solution_give_up:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
