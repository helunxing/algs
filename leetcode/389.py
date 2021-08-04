class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d=[0]*26
        for c in t:
            d[ord(c)-ord('a')]+=1
        for c in s:
            d[ord(c)-ord('a')]-=1
        for i in range(len(d)):
            if d[i]:
                return chr(i+ord('a'))
