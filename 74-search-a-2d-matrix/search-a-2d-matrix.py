class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m,n=len(matrix),len(matrix[0])
        l,r=0,m*n-1
        while l<=r:
            m=(l+r)//2
            mv=matrix[m//n][m%n]
            if mv==target:
                return True
            elif mv<target:
                l=m+1
            else:
                r=m-1
        return False
        