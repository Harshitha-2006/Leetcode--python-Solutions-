class Solution:
    def simplifyPath(self, path: str) -> str:
        s=[]
        for i in path.split('/'):
            if i=='' or i=='.':
                continue
            elif i=='..':
                if s:
                    s.pop()
            else:
                s.append(i)
        return '/'+'/'.join(s)
        