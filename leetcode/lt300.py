class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        lts = [nums[0]]
        for i in range(1, len(nums)):
            if lts[-1] < nums[i]:
                lts.append(nums[i])
            else:
                l, r = 0, len(lts)-1
                while l < r:
                    mid = l+(r-l)//2
                    if lts[mid] < nums[i]:
                        l = mid+1
                    else:
                        r = mid
                lts[l] = nums[i]
        return len(lts)

class Solution_v1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        dp = [0]*n
        max = 0

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = dp[j]+1 if dp[j]+1 > dp[i] else dp[i]
            if dp[i] > max:
                max = dp[i]

        return max+1
