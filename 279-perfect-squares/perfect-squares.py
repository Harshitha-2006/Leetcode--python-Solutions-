import math
from collections import deque
class Solution:
    def numSquares(self,n:int)->int:
        q=deque()
        q.append(n)
        height=0
        while q:
            height+=1
            for i in range(len(q)):
                num=q.popleft()
                for j in range(1,int(math.sqrt(num))+1):
                    if j*j==num:
                        return height
                    elif num-j*j>0:
                        q.append(num-j*j)
                    else:
                        break
