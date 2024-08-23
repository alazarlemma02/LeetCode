class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n==0: return True
        for flower in range(len(flowerbed)):
            if flowerbed[flower]==0 and (flower==0 or flowerbed[flower-1]==0) and (flower==len(flowerbed)-1 or flowerbed[flower+1]==0):
                flowerbed[flower]=1
                n-=1
                if n==0: return True
        return False
        