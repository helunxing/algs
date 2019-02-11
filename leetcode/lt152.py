class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:  # 第二次提交时想绕过本判断，但出现了强行赋0的问题。果然越界访问是万恶之源。
            return nums[0]

        dp_pos, dp_nag = [0]*(len(nums)), [0]*(len(nums))

        ans = nums[0]
        for i in range(len(nums)):
            if nums[i] > 0:
                dp_pos[i] = dp_pos[i-1]*nums[i] if dp_pos[i-1] else nums[i]
                dp_nag[i] = dp_nag[i-1]*nums[i]
            elif nums[i] < 0:
                # 第一次提交时下行在后面，如果数组长度为1时会导致自身相乘问题。
                dp_pos[i] = dp_nag[i-1]*nums[i]
                dp_nag[i] = dp_pos[i-1]*nums[i] if dp_pos[i-1] else nums[i]
            else:
                dp_nag[i] = 0
                dp_pos[i] = 0
            if dp_pos[i] > ans:
                ans = dp_pos[i]

        return ans
