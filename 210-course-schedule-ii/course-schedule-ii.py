from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        indegree=[0]*numCourses
        for a,b in prerequisites:
            g[b].append(a)
            indegree[a]+=1
        
        queue=deque([i for i in range(numCourses) if indegree[i]==0])
        order=[]
        while queue:
            c=queue.popleft()
            order.append(c)
            for i in g[c]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        
        return order if len(order) == numCourses else []
        