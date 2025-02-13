class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:


        l = len(flowerbed)
        can_plant = 0

        if l == 1 and flowerbed[0] == 0:
            can_plant += 1

        if l > 1:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                print("0 happened")
                flowerbed[0] = 1
                can_plant += 1
                print(can_plant)

        if l > 1:
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                print("l-1 happened")
                flowerbed[l-1] = 1
                can_plant += 1
                print(can_plant)

        for i in range(1,l-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                print("happened")
                can_plant += 1
                flowerbed[i] = 1
        

        
        print(n)
        print(can_plant)
        if can_plant >= n:
            return True
        
        return False


        