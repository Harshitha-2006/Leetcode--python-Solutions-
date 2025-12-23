class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a,b=0,0
        for i in (cost):
            a,b=b,min(a,b)+i
        return min(a,b)