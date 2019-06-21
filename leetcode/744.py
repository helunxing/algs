class Solution:
    def nextGreatestLetter(self, letters, target) -> str:
        l, r = 0, len(letters)-1
        while l < r:
            m = l+(r-l)//2
            if ord(target) < ord(letters[m]):
                r = m
            else:
                l = m+1
        return letters[0] if r == len(letters)-1 and \
            ord(letters[r]) <= ord(target) \
            else letters[r]


s = Solution()
print(s.nextGreatestLetter(["c", "f", "j"], "g"))
