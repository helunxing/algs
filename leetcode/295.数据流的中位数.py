#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxh = []
        self.minh = []
        heapq.heapify(self.maxh)
        heapq.heapify(self.minh)

    def addNum(self, num: int) -> None:
        if not self.maxh:
            heapq.heappush(self.maxh, -num)
            return
        if -self.maxh[0] < num:
            heapq.heappush(self.minh, num)
            if len(self.maxh) < len(self.minh):
                heapq.heappush(self.maxh, -heapq.heappop(self.minh))
        else:
            heapq.heappush(self.maxh, -num)
            if len(self.maxh) > len(self.minh):
                heapq.heappush(self.minh, -heapq.heappop(self.maxh))

    def findMedian(self) -> float:
        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()
        max_len = len(self.maxh)
        min_len = len(self.minh)
        if max_len == min_len:
            return (self.minh[0]-self.maxh[0])/2
        elif max_len > min_len:
            return -self.maxh[0]
        else:
            return self.minh[0]
