import heapq
import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        wndo, ans = [], []
        for i, x in enumerate(nums):
            if k <= i and wndo[0] <= i-k:
                wndo.pop(0)
            while wndo and nums[wndo[-1]] < x:
                wndo.pop()
            wndo.append(i)
            if i >= k-1:
                ans.append(nums[wndo[0]])
        return ans


class Solution1(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        n = len(nums)

        ans = []

        h_wndo = [-nums[i] for i in range(k)]
        heapq.heapify(h_wndo)
        h_wait = []
        heapq.heapify(h_wait)

        for i in range(n-k):
            ans.append(-heapq.nsmallest(1, h_wndo)[0])

            heapq.heappush(h_wait, -nums[i])
            heapq.heappush(h_wndo, -nums[k+i])

            while h_wait and heapq.nsmallest(1, h_wndo)[0] == heapq.nsmallest(1, h_wait)[0]:
                heapq.heappop(h_wait)
                heapq.heappop(h_wndo)

        ans.append(-heapq.nsmallest(1, h_wndo)[0])

        return ans


class Solution2(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)-k):
            wndo = nums[i:i+k]
            heapq.heapify(wndo)
            ans.append(heapq.heappop(wndo))

        return ans
