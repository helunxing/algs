class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res += [x+pow(2, i) for x in reversed(res)]
        return res
