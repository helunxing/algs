class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        sta = 0
        while sta < len(s):
            end = sta
            while end < len(s):
                if s[end] != s[sta]:
                    break
                end += 1
            if end-sta > 3:
                ans.append([sta, end-1])
            sta = end+1
        return ans
