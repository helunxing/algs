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

    def majorityElement_1903(self, nums: List[int]) -> int:
        cnt = 0
        candi = None
        for i in nums:
            if not cnt:
                candi = i
            cnt += 1 if candi == i else -1
        return candi
