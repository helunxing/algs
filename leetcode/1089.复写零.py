class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        def move(sta):
            end = len(arr)-1
            while end > sta:
                arr[end] = arr[end-1]
                end -= 1

        i = 0
        while i < len(arr):
            if arr[i] == 0:
                move(i)
                i += 1
            i += 1
