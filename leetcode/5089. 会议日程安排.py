class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        res = []
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            a, b = slots1[i], slots2[j]
            if a[0] > b[1]:
                j += 1
                continue
            if b[0] > a[1]:
                i += 1
                continue
            sta, end = max(a[0], b[0]), min(a[1], b[1])
            if sta+duration <= end:
                res = [sta, sta+duration]
                break
            if a[1] < b[1]:
                i += 1
            else:
                j += 1
        return res
