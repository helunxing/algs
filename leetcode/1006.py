class Solution:
    def clumsy(self, N: int) -> int:
        ans = 0
        huihe = N//4
        shengyu = N-N//4*4
        shu = huihe*4+shengyu
        ans = (shu)*(shu-1)//(shu-2)+(shu-3) if huihe else 0
        for i in range(huihe-1, 0, -1):
            shu = i*4+shengyu
            ans += -((shu)*(shu-1)//(shu-2))+(shu-3)
        shu = 4
        if shengyu == 3:
            ans += -((shu-1)*(shu-2)//(shu-3))
        elif shengyu == 2:
            ans += -(shu-2)*(shu-3)
        elif shengyu == 1:
            ans += -(shu-3)
        if N<4:
            return -ans
        return ans
    