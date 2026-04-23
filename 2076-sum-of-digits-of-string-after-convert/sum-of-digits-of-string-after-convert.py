class Solution:
    def getLucky(self, s: str, k: int) -> int:
        l=""
        for i in s:
            l+=str(ord(i)-ord('a')+1)
        for i in range(k):
            s=0
            for j in l:
                s+=int(j)
            l=str(s)
        return int(l)