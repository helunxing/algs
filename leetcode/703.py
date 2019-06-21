import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.size = len(nums)
        self.h = nums
        heapq.heapify(self.h)
        while self.size > k:
            heapq.heappop(self.h)
            self.size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heappop(self.h)
            heapq.heappush(self.h, val)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
