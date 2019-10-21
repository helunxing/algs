class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        for i in reversed(range(len(T)-1)):
            if T[i] < T[i+1]:
                res[i] = 1
            else:
                last = i+1
                while res[last] != 0:
                    last += res[last]
                    if T[last] > T[i]:
                        res[i] = last-i
                        break
        return res
