class Solution:
    def countBits(self, n: int) -> List[int]:
        b=[]
        for i in range(0,n+1):
            b.append(bin(i).count('1'))
        return b    
        