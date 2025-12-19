class Solution:
    def maximalSquare(self,matrix:List[List[str]])->int:
        m,n=len(matrix),len(matrix[0])
        scan=[0]*n
        l=0
        for r in range(m):
            cnt=0
            skip=False
            for c in range(n):
                if matrix[r][c]=="1":
                    scan[c]+=1
                else:
                    scan[c]=0
                if skip:
                    continue
                if scan[c]>l:
                    cnt+=1
                else:
                    cnt=0
                if cnt>l:
                    l+=1
                    skip=True
        return l**2
