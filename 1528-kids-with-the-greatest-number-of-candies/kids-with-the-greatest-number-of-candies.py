class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        r=[]
        for i in candies:
            x=i+extraCandies
            r.append(x>=m)
            x=0
        return r