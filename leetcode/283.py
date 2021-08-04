class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1


def test_a():
    a = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes(a)
    assert a == [1, 3, 12, 0, 0, 0]


def move(l):
    unzero, zero = len(l)-1, len(l)-1
    while unzero >= 0 and l[unzero] == 0:
        unzero -= 1
    while zero >= 0 and l[zero] != 0:
        zero -= 1

    while True:
        l[unzero], l[zero] = l[zero], l[unzero]
        # zero = len(l)-1
        # while zero >= 0 and l[zero] != 0:
        #     zero -= 1
        zero -= 1
        unzero -= 1
        while unzero >= 0 and l[unzero] == 0:
            unzero -= 1
        if unzero < 0 or zero <= unzero:
            return l

# print(move([0, 0]))

# print(move([4, 5]))

# print(move([0, 8, 5, 0, 134, 0, 3, 6, 5, 0, 7, 0]))

# test_a()
