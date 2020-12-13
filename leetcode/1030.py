class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        l = [[i, j]for i in range(R) for j in range(C)]
        l.sort(key=lambda x: abs(x[0]-R)+abs(x[1]-R))
        return l
