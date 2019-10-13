class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        wind = nums[:k]
        wind.sort()

        def mid():
            return wind[k//2] if k & 1 else wind[k//2-1]+(wind[k//2]-wind[k//2-1])/2

        res = [mid()]
        i = 0

        while i < len(nums)-k:
            ins = bisect.bisect_left(wind, nums[i])
            wind[ins] = nums[i+k]
            wind.sort()
            res.append(mid())
            i += 1

        return res
