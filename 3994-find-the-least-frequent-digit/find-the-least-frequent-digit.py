class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        d={}
        while n>0:
            i=n%10
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            n=n//10
        l=[]
        for i in d:
            l.append(d[i])
        x=min(l)
        res=9
        for i in d:
            if d[i]==x:
                res=min(res,i)
        return res