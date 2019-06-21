class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for x in s:
            if x-1 not in s:
                sta, end = x, x+1
                while end in s:
                    end += 1
                best = best if best > end-sta else end-sta
        return best
