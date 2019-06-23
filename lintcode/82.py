class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def singleNumber(self, A):
        # write your code here
        tmp = 0
        for i in A:
            tmp ^= i
        return tmp
