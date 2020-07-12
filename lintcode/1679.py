class Solution:
    """
    @param n str: the number n
    @return str: the smallest lucky number  that is not less than n
    """

    def luckyNumber(self, n):
        # Write your code here.
        if len(n) & 1 or int(n[0]) > 5:
            return '3'*((len(n)+1)//2)+'5'*((len(n)+1)//2)

        s = []
        cnt5 = len(n)//2
        i = 0
        # enled = False

        while i < len(n) and cnt5 > 0:
            num = int(n[i])
            if num < 3:
                s += [3]*(len(n)-len(s)-cnt5)+[5]*cnt5
            elif num == 3:
                s.append(3)
            elif num == 4:
                s.append(5)
                cnt5 -= 1
                s += [3]*(len(n)-len(s)-cnt5)+[5]*cnt5
            elif num == 5:
                s.append(5)
                cnt5 -= 1
            else:
                if int(n[i-1]) == 4:
                    s[-1] = 5
                    cnt5-1
                    s += [3]*(len(n)-len(s)-cnt5)+[5]*cnt5
                else:
                    return '3'*((len(n))//2+1)+'5'*((len(n))//2+1)
            i += 1

        if len(s) != len(n):
            return '3'*((len(n))//2+1)+'5'*((len(n))//2+1)

        res = ''
        for i in s:
            res += str(i)
        return res
