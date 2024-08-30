class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for x in range(len(flowerbed)):

            left_point = (x == 0) or (flowerbed[x-1] == 0)
            right_point = (x < len(flowerbed)) or (flowerbed[x + 1] == 0)

            if left_point and right_point:
                n -= 1
        
        print(n)
        if n == 0:
            return True
        else:
            return False
        
                