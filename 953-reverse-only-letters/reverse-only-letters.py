class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a=[]
        o=[]
        l=[]
        for i in reversed(s):
            if i.isalpha():
                a.append(i)
        j=0
        for i in s:
            if i.isalpha():
                l.append(a[j])
                j+=1
            else:
                l.append(i)
        return "".join(l)
        