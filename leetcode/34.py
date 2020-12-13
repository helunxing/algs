class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        l, r = 0, len(nums)-1
        while l < r:
            m = l+(r-l)//2
            if nums[m] < target:
                l = m+1
            else:
                r = m
        s = r if nums[r] == target else -1

        l, r = 0, len(nums)-1
        while l < r:
            m = l+(r-l+1)//2
            if nums[m] <= target:
                l = m
            else:
                r = m-1
        e = l if nums[l] == target else -1

        return [s, e]
