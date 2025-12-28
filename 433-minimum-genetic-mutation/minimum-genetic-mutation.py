from collections import deque

class Solution:
    def minMutation(self,start:str,end:str,bank:List[str])->int:
        def i(node):
            res=[]
            for j in range(len(node)):
                for g in ["A","C","G","T"]:
                    if node[j]!=g:
                        res.append(node[:j]+g+node[j+1:])
            return res
        b=set(bank)
        if end not in b:
            return -1
        q=deque([(start,0)])
        seen={start}
        while q:
            node,s=q.popleft()
            if node==end:
                return s
            for n in i(node):
                if n not in seen and n in b:
                    seen.add(n)
                    q.append((n,s+1))
        return -1
