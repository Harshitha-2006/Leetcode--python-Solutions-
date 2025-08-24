class Solution:
    def decodeString(self, s: str) -> str:
        n=0
        st=[]
        r=''
        for i in s:
            if i.isdigit():
                n=n*10+int(i)
            elif i=='[':
                st.append((r,n))
                r=''
                n=0
            elif i.isalpha():
                r+=i
            elif i==']':
                x,y=st.pop()
                r=x+y*r
        return r
        