class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        if not nums:
            return res
        l,r=0,len(nums)-1
        i=-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                i=m
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        if i==-1:
            return res
        else:
            res[0]=i
            x=i+1
            while x<len(nums) and nums[x-1]==nums[x]:
                x=x+1
            if x==i+1:
                res[1]=i
            else:
                res[1]=x-1
        return res
        