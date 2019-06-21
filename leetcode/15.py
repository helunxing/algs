# 答案可以分成四种：正负零，三零，两正一负，两负一正
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pos_dic, nag_dic = {}, {}
        zero_times = 0

        for num in nums:
            if num > 0:
                pos_dic[num] = pos_dic.get(num, 0)+1
            elif num < 0:
                nag_dic[num] = nag_dic.get(num, 0)+1
            else:
                zero_times += 1

        self.ans = []

        if zero_times >= 3:  # 三零
            self.ans.append([0, 0, 0])

        if zero_times != 0:  # 正负零
            for num in pos_dic:
                if nag_dic.get(-num, 0) != 0:
                    self.ans.append([num, 0, -num])

        self.two_one(pos_dic, nag_dic)  # 两正
        self.two_one(nag_dic, pos_dic)  # 两负
        return self.ans

    def two_one(self, dic_two, dic_one):
        nums_list = dic_two.keys()
        for i in range(len(nums_list)):
            num_a = nums_list[i]
            if dic_two[num_a] >= 2 and dic_one.get(-num_a*2, 0) != 0:
                self.ans.append([num_a, num_a, -num_a*2])  # 两个相同
            for j in range(i+1, len(nums_list)):
                num_b = nums_list[j]
                if dic_one.get(-num_a-num_b, 0) != 0:
                    self.ans.append([num_a, num_b, -num_a-num_b])
# 时间 n^2
# 空间 n


class Solution2:
    # 2019年3月8日 稠了加水算法
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 40
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                tmp = nums[i]+nums[j]+nums[k]
                if tmp < 0:
                    j += 1
                elif tmp > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while True:
                        j += 1
                        if j+1 >= len(nums) or nums[j-1] != nums[j]:
                            break
                    while True:
                        k -= 1
                        if k-1 <= i or nums[k+1] != nums[k]:
                            break
        return ans
        # 00
