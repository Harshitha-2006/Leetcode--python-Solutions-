class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r=[]
        def backtrack(start,p,t):
            if t==target:
                r.append(p[:])
                return 
            if t>target:
                return
            for i in range(start,len(candidates)):
                p.append(candidates[i])
                backtrack(i,p,t+candidates[i])
                p.pop()
        backtrack(0,[],0)
        return r
        