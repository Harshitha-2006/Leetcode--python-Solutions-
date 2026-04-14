class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        l=[]
        s=''
        for i in word:
            if i.isdigit():
                s+=i
            else:
                if s:
                    l.append(str(int(s)))
                    s=''
        if s:
            l.append(str(int(s)))
        return len(set(l))