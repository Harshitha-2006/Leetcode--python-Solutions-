class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        for i in s:
            if i.isalpha():
                pass
            else:
                l.append(i)
        s=list(set(l))
        s=sorted(s)
        if len(s)<=1:
            return -1
        else:
            x=s[-2]
            return int(x)