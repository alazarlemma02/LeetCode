class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n==0:
            return True
        m_flowerbed = [0] + flowerbed + [0]
        for flower in range(1, len(m_flowerbed)-1):
            if m_flowerbed[flower-1]==0 and m_flowerbed[flower+1]==0 and m_flowerbed[flower]==0:
                m_flowerbed[flower] = 1
                n-=1
                if n==0:
                    return True
        return False
        