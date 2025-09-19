class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start:int,comb:List[int],total:int):
            if len(comb)==k and total==n:
                res.append(comb[:])
                return
            if len(comb)>k or total>n:
                return
            for i in range(start,10):
                comb.append(i)
                backtrack(i+1,comb,total+i)
                comb.pop()
        res=[]
        backtrack(1,[],0)
        return res
        