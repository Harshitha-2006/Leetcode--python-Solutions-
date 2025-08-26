class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r=[]
        def back(c,l,right):
            if len(c)==2*n:
                r.append(c)
                return
            if l<n:
                back(c+'(',l+1,right)
            if right<l:
                back(c+')',l,right+1)
        back("",0,0)
        return r
        