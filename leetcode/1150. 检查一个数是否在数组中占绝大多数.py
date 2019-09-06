class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        app = 0
        for i in nums:
            if i == target:
                app += 1

        return app > len(nums)//2

