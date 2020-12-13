class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5: 0, 10: 0, 20: 0}
        for m in bills:
            dic[m] += 1
            if m == 10:
                dic[5] -= 1
                if dic[5] < 0:
                    return False
            elif m == 20:
                if dic[10] > 0 and dic[5] > 0:
                    dic[10] -= 1
                    dic[5] -= 1
                elif dic[5] > 2:
                    dic[5] -= 3
                else:
                    return False
        return True
