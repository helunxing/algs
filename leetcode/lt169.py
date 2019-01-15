class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            d[i] = d.setdefault(i, 0)+1
        max = nums[0]
        for key in d:
            if d[max] < d[key]:
                max = key
        return max


s = Solution()
s.majorityElement([1, 2, 3, 4])
