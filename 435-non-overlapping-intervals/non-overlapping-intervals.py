class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        c=0
        e=float('-inf')
        for i in intervals:
            if i[0]<e:
                c+=1
            else:
                e=i[1]
        return c
        