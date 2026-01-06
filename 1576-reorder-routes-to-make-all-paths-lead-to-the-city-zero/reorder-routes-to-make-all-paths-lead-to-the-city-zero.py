class Solution:
    def minReorder(self, n: int, connections: List[List[int]])-> int:
        g=defaultdict(list)
        for a,b in connections:
            g[a].append((b,1))
            g[b].append((a,0))
        def dfs(location,parent):
            res=0
            for c,d in g[location]:
                if c==parent:continue
                res+=d+dfs(c,location)
            return res
        return dfs(0,0)
