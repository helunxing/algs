class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        ji, ou = nums[:], nums[:]
        resj, reso = 0, 0

        for i in range(0, l, 2):
            if i == 0:
                edge = nums[1]
            elif i == l-1:
                edge = nums[l-2]
            else:
                edge = min(nums[i-1], nums[i+1])
            reso += nums[i]-edge+1 if nums[i] >= edge else 0
            ou[i] = edge-1 if nums[i] >= edge else ou[i]

        for i in range(1, l, 2):
            if i == 0:
                edge = nums[1]
            elif i == l-1:
                edge = nums[l-2]
            else:
                edge = min(nums[i-1], nums[i+1])
            resj += nums[i]-edge+1 if nums[i] >= edge else 0
            ji[i] = edge-1 if nums[i] >= edge else ji[i]

        return min(resj, reso)
