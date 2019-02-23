class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        self.NSum(ans, [], 4, nums, target)
        return ans

    def NSum(self, ans, used, n, nums, target):
        if len(nums) < n or n < 2:
            return
        if n == 2:
            f = 0
            r = len(nums)-1
            while f < r:
                if nums[f]+nums[r] < target:
                    f += 1
                elif nums[f]+nums[r] > target:
                    r -= 1
                else:
                    ans.append(used+[nums[f], nums[r]])
                    while f < r and nums[f] == nums[f+1]:
                        f += 1
                    while f < r and nums[r] == nums[r-1]:
                        r -= 1
                    f += 1
            return
        for i in range(len(nums)):
            if target < nums[i]*n or target > nums[-1]*n:
                break
            if i == 0 or i > 0 and nums[i-1] != nums[i]:
                self.NSum(ans, used+[nums[i]], n-1, nums[i+1:], target-nums[i])


s = Solution()
ans = s.fourSum([1, 0, -1, 0, -2, 2], 0)
pass
