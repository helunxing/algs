import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(h, nums[i])
            else:
                if nums[i] > h[0]:
                    heapq.heappop(h)
                    heapq.heappush(h, nums[i])

        return h[0]
