class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        o, t = len(num1), len(num2)
        ans_n = [0]*(o+t)

        for i in range(o):
            for j in range(t):
                ans_n[i+j+1] += (ord(num1[i])-ord('0')) * \
                    (ord(num2[j])-ord('0'))

        for i in range(o+t-1, 0, -1):
            ans_n[i-1] += ans_n[i]//10
            ans_n[i] %= 10

        sta = 0
        while not ans_n[sta]:
            sta += 1
        ans = ''
        for i in range(sta, o+t):
            ans += chr(ord('0')+ans_n[i])

        return ans
