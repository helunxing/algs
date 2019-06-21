class Solution:
    def search(self, nums, target) -> int:
        if not nums:
            return -1
        f, r = 0, len(nums)-1
        while f <= r:
            m = f+(r-f)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                f = m+1
            else:
                return m

        return -1


s = Solution()
s.search([-1, 0, 5], 0)
s.search([-1, 0, 3, 5, 9, 12], 9)
