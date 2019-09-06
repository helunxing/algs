class Solution:
    def minSwaps(self, data: List[int]) -> int:
        l = sum(data)
        tmp = sum(data[:l])
        rem = tmp
        for e in range(l, len(data)):
            s = e-l
            tmp += data[e]-data[s]
            rem = max(rem, tmp)
        return l-rem
