class Solution:
    def defangIPaddr(self, address: str) -> str:
        l=[]
        for i in address:
            if i.isalnum():
                l.append(i)
            else:
                l.append("[.]")
        return "".join(l)