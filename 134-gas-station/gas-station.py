class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        n=len(gas)
        d=[]
        for i in range(n):
            x=gas[i]-cost[i]
            d.append(x)
        t=0
        r=0
        for i in range(n):
            t+=d[i]
            if t<0:
                r=i+1
                t=0
        return r