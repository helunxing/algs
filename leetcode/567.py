class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 00
        def ctn(i):
            return ord(i)-ord('a')
        st = [0]*26  # stand
        cp = [0]*26  # current present
        ll = 0  # last length
        ma = 0
        for i in s1:
            st[ctn(i)] += 1
        for i, x in enumerate(s2):
            if not st[ctn(x)]:
                for i in range(26):
                    cp[i] = 0
                ll = 0
                continue
            if cp[ctn(x)] == st[ctn(x)]:
                while cp[ctn(x)] == st[ctn(x)]:
                    cp[ctn(s2[i-ll])] -= 1
                    ll -= 1
            cp[ctn(x)] += 1
            ll += 1
            ma = ll if ll > ma else ma
        return ma == len(s1)
        # 29
