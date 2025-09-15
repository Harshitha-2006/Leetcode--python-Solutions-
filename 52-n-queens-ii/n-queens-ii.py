class Solution:
    def totalNQueens(self, n: int) -> int:
        c=set()
        p=set()
        neg=set()
        res=[]
        board=[["."]*n for i in range(n)]
        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for col in range(n):
                if col in c or(r+col) in p or(r-col) in neg:
                    continue
                c.add(col)
                p.add(r+col)
                neg.add(r-col)
                board[r][col]="Q"
                backtrack(r+1)
                c.remove(col)
                p.remove(r+col)
                neg.remove(r-col)
                board[r][col]="."
        backtrack(0)
        return len(res)