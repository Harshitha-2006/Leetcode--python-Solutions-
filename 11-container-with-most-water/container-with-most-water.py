class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        g=0
        if len(height)==2:
            return min(height)
        while l<r:
            a=min(height[l],height[r])*(r-l)
            if g<=a:
                g=a
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return g
        