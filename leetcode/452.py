class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        ans = 1
        curr = points[0][1]

        for s, e in points:
            if curr < s:
                ans += 1
                curr = e
                continue

            if e < curr:
                curr = e

        return ans
