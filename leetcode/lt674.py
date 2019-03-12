class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        if not nums:
            return 0
        cont = 1
        maxc = cont
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cont += 1
                maxc = cont if cont > maxc else maxc
            else:
                cont = 1
        return maxc


s = Solution()
s.findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5])
