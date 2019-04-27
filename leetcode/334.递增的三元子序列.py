#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#


class Solution:
    def increasingTriplet(self, nums) -> bool:
        if not nums:
            return False
        pre_que = [nums[0]]
        for i in range(1, len(nums)):
            wait = nums[i]
            if pre_que[-1] < wait:
                pre_que.append(wait)
                if len(pre_que) == 3:
                    return True
            else:
                l, r = 0, len(pre_que)-1
                while l < r:
                    m = l+(r-l)//2
                    if pre_que[l] < wait:
                        l = m+1
                    else:
                        r = m
                pre_que[l] = min(wait, pre_que[l])
        return False
