class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        a=1
        p=points[0][1]
        for s,e in points[1:]:
            if s>p:
                a+=1
                p=e
        return a
        