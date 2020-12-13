class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def mycmp(x):
            return (0, rank[x]) if x in rank else (1, x)
        rank = {x: i for i, x in enumerate(arr2)}
        arr1.sort(key=mycmp)
        return arr1


class Solution0:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []

        i = 0
        while i < len(arr2):
            j = 0
            while j < len(arr1):
                if arr1[j] == arr2[i]:
                    res.append(arr1[j])
                    del arr1[j]
                else:
                    j += 1
            i += 1

        res = res+sorted(arr1)

        return res
