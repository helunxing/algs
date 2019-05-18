#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前K个高频元素
#

import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
