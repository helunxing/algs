class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        d = {}
        for i, x in enumerate(numbers):
            if x in d:
                return [d[x], i]
            d[target-x] = i


s = Solution()
ans=s.twoSum([2, 7, 11, 15], 9)
pass
