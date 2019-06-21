class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 22
        l, r = 0, len(height)-1
        smax = 0
        while l < r:
            dire = height[l] > height[r]
            s = height[r]*(r-l) if dire else height[l]*(r-l)
            smax = s if s > smax else smax
            if dire:
                r -= 1
            else:
                l += 1
        return smax
        # 27
