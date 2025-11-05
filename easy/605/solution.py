class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            return n == 1

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n = n - 1

        if n == 0:
            return True

        for idx in range(1,len(flowerbed)-1):
            if flowerbed[idx-1] == 0 and flowerbed[idx] == 0 and flowerbed[idx+1] == 0:
                n = n - 1
                flowerbed[idx] = 1
            if n == 0:
                return True

        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
            n = n - 1
        return n==0
    