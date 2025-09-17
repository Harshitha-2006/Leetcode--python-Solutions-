from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d=defaultdict(int)
        c=0
        for row in grid:
            d[tuple(row)]+=1 
        for col in zip(*grid):
            c+=d[tuple(col)]
        return c\
    