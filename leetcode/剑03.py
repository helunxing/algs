class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)
        return 0
        