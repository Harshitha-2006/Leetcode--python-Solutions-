from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        g=[]
        for i in range(numCourses):
            g.append([])
        d=[0]*numCourses
        for a,b in prerequisites:
            g[b].append(a)
            d[a]+=1
        q=deque()
        for i in range(numCourses):
            if d[i]==0:
                q.append(i)
        c=0
        while q:
            course=q.popleft()
            c+=1
            for nc in g[course]:
                d[nc]-=1
                if d[nc]==0:
                    q.append(nc)
        return c==numCourses
