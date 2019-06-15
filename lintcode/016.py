class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here

        def dfs(res, temp, nums):
            if nums == []:
                res += [temp]
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    dfs(res, temp+[nums[i]], nums[:i]+nums[i+1:])
        if nums == None:
            return []
        # if len(nums) == 0:
            # return [[]]
        res = []
        dfs(res, [], sorted(nums))
        return res
