class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        s = []
        n = len(height)
        for curr in range(n):
            while s and height[curr] > height[s[-1]]:
                top = s.pop()
                if not s:
                    break
                distance = curr-s[-1]-1
                bon_hei = min(height[curr], height[s[-1]])-height[top]
                ans += distance*bon_hei
            s.append(curr)
        return ans
