# from functools import reduce
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return nums and [s[:i]+[nums[0]]+s[i:]
        #                  for s in self.permute(nums[1:])
        #                  for i in range(len(nums))] or [[]]
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
