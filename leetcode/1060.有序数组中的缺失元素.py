class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        ans, curr, cnt = nums[0], 1, k
        while cnt > 0:
            diff = nums[curr]-ans-1 if curr < len(nums) else cnt
            if diff < cnt:
                cnt -= diff
                ans = nums[curr]
                curr += 1
            else:
                ans += cnt
                cnt -= cnt
        return ans
