import numpy as np
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        z=[]
        for i in matrix:
            if 0 in i:
                for j in range(len(i)):
                    if i[j]==0:
                        z.append(j)
                    i[j]=0
        for i in matrix:
            for j in z:
                i[j]=0

        