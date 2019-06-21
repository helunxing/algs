class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        one_prese = False

        for i in range(len(nums)):
            if nums[i] == 1:
                one_prese = True
            if nums[i] <= 0 or len(nums) < nums[i]:
                nums[i] = 1

        if not one_prese:
            return 1

        for i in range(len(nums)):
            if nums[i] > 0:
                mark_ = nums[i]-1
            else:
                mark_ = -nums[i]-1
            if nums[mark_] > 0:
                nums[mark_] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1

        return len(nums)+1
