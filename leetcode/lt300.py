class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n=len(nums)
        dp=[0]*n
        max=0
        
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=dp[j]+1 if dp[j]+1>dp[i] else dp[i]
            if dp[i]>max:
                max=dp[i]
                
        return max+1
    