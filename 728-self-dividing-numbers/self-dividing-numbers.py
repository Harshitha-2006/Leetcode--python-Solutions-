class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range(left,right+1):
            s=0
            dd=[]
            x=i
            while x>0:
                d=x%10
                s=s*10+d
                dd.append(d)
                x=x//10
            for j in dd:
                if j==0 or i%j!=0:
                    break
            else:
                l.append(i)
        return l
            