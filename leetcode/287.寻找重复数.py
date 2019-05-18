#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if finder == slow:
                return finder
