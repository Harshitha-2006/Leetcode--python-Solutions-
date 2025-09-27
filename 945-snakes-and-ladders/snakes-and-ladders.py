from collections import deque
from typing import List
class Solution:
    def snakesAndLadders(self,board:List[List[int]])->int:
        n=len(board)
        def get_position(s):
            r=(s-1)//n
            c=(s-1)%n
            if r%2:
                c=n-1-c
            return n-1-r,c
        q=deque()
        q.append((1,0))
        visited=set()
        visited.add(1)
        while q:
            s,moves=q.popleft()
            for i in range(1,7):
                n_=s+i
                if n_>n*n:
                    continue
                r,c=get_position(n_)
                if board[r][c]!=-1:
                    n_=board[r][c]
                if n_==n*n:
                    return moves+1
                if n_ not in visited:
                    visited.add(n_)
                    q.append((n_,moves+1))
        return -1
