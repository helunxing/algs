class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 09
        nums.sort()
        nest = nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j != k:
                tmp = nums[i]+nums[j]+nums[k]
                nest = nest if abs(tmp-target) > abs(nest-target) else tmp
                if tmp > target:
                    k -= 1
                else:
                    j += 1
        return nest
