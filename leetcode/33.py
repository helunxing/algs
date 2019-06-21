class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l <= r:
            m = l+(r-l)//2
            if nums[m] == target:
                return m
            if nums[m] <= nums[r]:
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
        return -1


s = Solution()
# ans = s.search([4, 5, 6, 7, 0, 1, 2], 3)
# ans2 = s.search([3, 1], 3)
# ans4 = s.search([1], 0)
ansf = s.search([1, 2], 2)
pass
