#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#


import random
import collections


class Solution:

    def findKthsmallest(self, nums, k: int) -> int:

        n = len(nums)

        def parti(sta, end):
            l, r = sta, end
            sel = random.randint(l, r)
            nums[r], nums[sel] = nums[sel], nums[r]

            pivot, pi = nums[r], r

            r -= 1
            while l < r:
                while l < r and nums[l] < pivot:
                    l += 1
                while l < r and pivot < nums[r]:
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] <= nums[pi]:
                l += 1
            nums[l], nums[pi] = nums[pi], nums[l]
            pi = l

            if pi < k-1:
                parti(pi, end)
            if k-1 < pi:
                parti(sta, pi)

        parti(0, n-1)
        return nums[k-1]

    def findKthLargest(self, nums, k: int) -> int:
        def parti(sta, end):
            np = random.randint(sta, end)
            l, r = sta, end

            nums[np], nums[r] = nums[r], nums[np]
            pivot, pi = nums[r], r
            r -= 1

            while l < r:
                while l < r and nums[l] >= pivot:
                    l += 1
                while l < r and nums[r] <= pivot:
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]

            if nums[l] > pivot:
                l += 1
            nums[l], nums[pi] = nums[pi], nums[l]
            pi = l

            if pi < k-1:
                parti(pi+1, end)
            if k-1 < pi:
                parti(sta, pi-1)

        parti(0, len(nums)-1)

        return nums[k-1]


s = Solution()
s.findKthLargest([3, 3, 3, 3, 3, 3, 3, 3, 3], 1)
