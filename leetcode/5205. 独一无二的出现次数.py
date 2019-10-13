class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cishu = [0]*2001
        for i in arr:
            cishu[i+1000] += 1

        cishu.sort(reverse=True)
        for i in range(len(cishu)-1):
            if cishu[i] == 0:
                break
            if cishu[i] == cishu[i+1]:
                return False
        return True
