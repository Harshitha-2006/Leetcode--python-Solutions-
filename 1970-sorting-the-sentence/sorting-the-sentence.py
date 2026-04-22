class Solution:
    def sortSentence(self, s: str) -> str:
        l=[""]*50
        r=""
        for i in s:
            if i.isalpha():
                r+=i
            elif i.isdigit():
                x=int(i)
                l[x]=r
                r=""
        return " ".join(w for w in l if w)