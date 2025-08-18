class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        r=[]
        if not nums:
            return r
        s=nums[0]
        for i in range(1,len(nums)+1):
            if i==len(nums) or nums[i]!=nums[i-1]+1:
                e=nums[i-1]
                if s==e:
                    r.append(str(s))
                else:
                    r.append(f"{s}->{e}")
                if i<len(nums):
                    s=nums[i]
        return r
        