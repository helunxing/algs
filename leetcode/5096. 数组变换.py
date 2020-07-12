class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        last = arr
        curr = [0] * len(arr)
        change = True
        while change:
            change = False
            curr[0], curr[-1] = last[0], last[-1]
            for i in range(1, len(arr) - 1):
                if last[i - 1] > last[i] < last[i + 1]:
                    curr[i] = last[i] + 1
                    change = True
                elif last[i - 1] < last[i] > last[i + 1]:
                    curr[i] = last[i] - 1
                    change = True
                else:
                    curr[i] = last[i]
            last, curr = curr, [0] * len(arr)
        return last
