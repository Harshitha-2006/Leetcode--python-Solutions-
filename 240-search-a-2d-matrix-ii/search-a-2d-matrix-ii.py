class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,col=len(matrix),len(matrix[0])
        for i in matrix:
            l,r=0,len(i)-1
            while l<=r:
                m=(l+r)//2
                if i[m]==target:
                    return True
                if i[m]>target:
                    r=m-1
                else:
                    l=m+1
        return False
