class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        t=0
        m=float('inf')
        for r in range(len(nums)):
            t+=nums[r]
            while target<=t:
                m=min(m,r-l+1)
                t-=nums[l]
                l+=1
        if(m==float('inf')):
            return 0
        else:
            return m

        