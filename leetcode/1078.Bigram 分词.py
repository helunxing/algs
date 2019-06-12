class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        n = len(words)
        res = []
        for i in range(n):
            if words[i] == first:
                if i+2 < n and words[i+1] == second:
                    res.append(words[i+2])
        return res
