class Solution:
    def missingNumber(self, arr) -> int:
        gap = (arr[-1]-arr[0])//(len(arr))
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] != gap:
                return arr[i]+gap
        return 0