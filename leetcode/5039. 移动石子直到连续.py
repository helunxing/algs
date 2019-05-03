class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        l = [a, b, c]
        l.sort()
        min_m = (1 if l[0] < l[1]-1 else 0) + (1 if l[1]+1 < l[2] else 0)
        if l[0] == l[1]-2 or l[1] == l[2]-2:
            min_m = 1
        max_m = l[1]-l[0]-1+l[2]-l[1]-1
        return [min_m, max_m]
