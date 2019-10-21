class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def j(x):
            k, s = K, 0
            for swt in sweetness:
                s += swt
                if s >= x:
                    k -= 1
                    s = 0
            return k < 0
        l, h = 0, sum(sweetness)//(K+1)
        while l < h:
            m = l+(h-l+1)//2
            if j(m):
                l = m
            else:
                h = m-1

        return l
