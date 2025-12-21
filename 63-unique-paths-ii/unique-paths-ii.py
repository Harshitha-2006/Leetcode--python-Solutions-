class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp={}
        def dfs(r,c):
            if r>=m or c>=n or obstacleGrid[r][c]:
               return 0
            if r==m-1 and c==n-1:
                return 1
            if (r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)]=dfs(r+1,c)+dfs(r,c+1)
            return dp[(r,c)]
        return dfs(0,0)