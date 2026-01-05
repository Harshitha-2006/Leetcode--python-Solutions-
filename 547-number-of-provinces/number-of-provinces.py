class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visit=[False]*n
        def dfs(city):
            visit[city]=True
            for nei in range(n):
                if isConnected[city][nei]==1 and not visit[nei]:
                    dfs(nei)
        provinces=0
        for i in range(n):
            if not visit[i]:
                provinces+=1
                dfs(i)
        return provinces