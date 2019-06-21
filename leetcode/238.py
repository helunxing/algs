class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 34
        ans = []
        n = len(nums)
        p = 1
        for i in range(n):
            ans.append(p)
            p *= nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            ans[i] *= p
            p *= nums[i]
        # 54
        return ans
