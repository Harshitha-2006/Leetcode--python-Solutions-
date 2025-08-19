class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c,p=0,0
        for i in flowerbed:
            if i==1:
                if p==1:
                    c-=1
                p=1
            else:
                if p==1:
                    p=0
                else:
                    c+=1
                    p=1
        return c>=n
        