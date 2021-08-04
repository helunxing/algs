class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        cnt = 0
        for i, x in enumerate(flowerbed):
            if x == 1:
                continue
            if i > 0 and flowerbed[i-1] == 1:
                continue
            if i < len(flowerbed)-1 and flowerbed[i+1] == 1:
                continue
            flowerbed[i] = 1
            cnt += 1
        return cnt >= n
