from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l=[]
        d={}
        res=[]
        n=len(grid)
        l1=[]       
        for i in range(1,(n*n)+1):
            l.append(i)
        for i in range(n):
                for j in range(n):
                    l1.append(grid[i][j])
        d=Counter(l1)
        for i in l:
            if d[i]>=2:
                res.append(i)
        for i in l:
            if i not in l1:
                res.append(i)
                break
        return res
        