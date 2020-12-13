class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()

        ans = 0
        for i in range(len(nums)-1):
            ans = nums[i+1]-nums[i] if nums[i+1]-nums[i] > ans else ans
        return ans
