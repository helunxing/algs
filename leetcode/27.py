class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        while j < len(nums):
            while i < len(nums) and nums[i] != val:
                i += 1
            j = i
            while j < len(nums) and nums[j] == val:
                j += 1
            if j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]

        return i-1
